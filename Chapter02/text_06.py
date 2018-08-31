txt = """And he looked over at the alarm clock,
ticking on the chest of drawers. "God in Heaven!" he thought.
It was half past six and the hands were quietly moving forwards,
it was even later than half past, more like quarter to seven.
Had the alarm clock not rung? He could see from the bed that it
had been set for four o'clock as it should have been; it certainly must have rung.
Yes, but was it possible to quietly sleep through that furniture-rattling noise?
True, he had not slept peacefully, but probably all the more deeply because of that."""

import string
trans = str.maketrans('', '', string.punctuation)
print(txt.lower().translate(trans))