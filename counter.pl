#!/usr/bin/perl
use warnings;
use strict;

my $string = do {
  local $/ = undef;
  open my $fh, "<", "count.txt"
  or die "Could not open count.txt: $!";
  <$fh>;
};

print "Current Total: " . $string . "\n";
print "How much to add?\n";

# read continuously
while (<>) {
  my $string = do {
    local $/ = undef;
    open my $fh, "<", "count.txt"
    or die "Could not open count.txt: $!";
    <$fh>;
  };
  $string += $_;
  $string += 0;
  open my $count, '>', 'count.txt';
  print {$count} $string;
  print "Current Total: " . $string . "\n";
}