import ftplib


class FTPCLient:
    def __init__(self, host, username='', password=''):
        self._client = ftplib.FTP_TLS(timeout=10)
        self._client.connect(host)

        # enable TLS
        try:
            self._client.auth()
        except ftplib.error_perm:
            # TLS authentication not supported
            # fallback to a plain FTP client
            self._client.close()
            self._client = ftplib.FTP(timeout=10)
            self._client.connect(host)
        
        self._client.login(username, password)

        if hasattr(self._client, 'prot_p'):
            self._client.prot_p()

    def cwd(self, directory):
        """Enter directory"""
        self._client.cwd(directory)

    def dir(self):
        """Returns list of files in current directory.

        Each entry is returned as a tuple of two elements,
        first element is the filename, the second are the
        properties of that file.
        """
        entries = []
        for idx, f in enumerate(self._client.mlsd()):
            if idx == 0:
                # First entry is current path
                continue
            if f[0] in ('..', '.'):
                continue
            entries.append(f)
        return entries

    def download(self, remotefile, localfile):
        """Download remotefile into localfile"""
        with open(localfile, 'wb') as f:
            self._client.retrbinary('RETR %s' % remotefile, f.write)

    def upload(self, localfile, remotefile):
        """Upload localfile to remotefile"""
        with open(localfile, 'rb') as f:
            self._client.storbinary('STOR %s' % remotefile, f)



cli = FTPCLient('localhost', username=USERNAME, password=PASSWORD)
print(
    cli.dir()
)
with open('/tmp/hello.txt', 'w+') as f:
    f.write('Hello World!')

cli.upload('/tmp/hello.txt', 'hellofile.txt')    
cli.download('hellofile.txt', '/tmp/hello2.txt')

with open('/tmp/hello2.txt') as f:
    print(f.read())