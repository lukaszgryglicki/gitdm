#
# Pull together regular expressions used in multiple places.
#
import re

#
# Some people, when confronted with a problem, think "I know, I'll use regular
# expressions." Now they have two problems.
#    -- Jamie Zawinski
#
Pcommit = re.compile (r'^commit ([0-9a-f ]+)$')
Pauthor = re.compile (r'^Author: ([^<]+)\s<([^>]+)>$')
Psob = re.compile (r'Signed-off-by:\s+([^<]+)\s+<([^>]+)>')
Pmerge = re.compile (r'^Merge:.*$')
Padd = re.compile (r'^\+[^\+].*$')
Prem = re.compile (r'^-[^-].*$')
Pdate = re.compile (r'^(Commit)?Date:\s+(.*)$')
Pfilea = re.compile (r'^---\s+(.*)$')
Pfileb = re.compile (r'^\+\+\+\s+(.*)$')

#
# Merges are described with a variety of lines.
#
PExtMerge = re.compile(r'^ +Merge( branch .* of)? ([^ ]+)\n$')
PIntMerge = re.compile(r'^ +(Merge|Pull) .* into .*$')
PIntMerge2 = re.compile(r"^ +Merge branch(es)? '.*$")