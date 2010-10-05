#format string
x = "There are %d types of people." % 10
binary = "binary"
#mixed type
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# o/p = string with quotes: exactly not value
print "I said: %r." % x

#double quotes = same as above #
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#adding format string arguments later
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#string concatenation
print w + e
