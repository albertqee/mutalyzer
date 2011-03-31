#!/usr/bin/env python

"""
Command-line interface to the nomenclature checker.

Usage:
  ./check 'AB026906.1:c.274delG'

@todo: Refactor this file.
"""


import sys
import os
import Mutalyzer
from Modules import Output
from Modules import Config


def main(cmd):
    """
    Command line interface to the name checker.

    @todo: documentation
    """
    C = Config.Config()
    O = Output.Output(__file__, C.Output)

    O.addMessage(__file__, -1, "INFO", "Received variant " + cmd)

    RD = Mutalyzer.process(cmd, C, O)

    O.addMessage(__file__, -1, "INFO", "Finished processing variant " + cmd)

    ### OUTPUT BLOCK ###
    gn = O.getOutput("genename")
    if gn :
        print "Gene Name: " + gn[0]
    tv = O.getOutput("transcriptvariant")
    if tv :
        print "Transcript variant: " + tv[0]
        print
    #if

    for i in O.getMessages() :
        print i
    errors, warnings, summary = O.Summary()
    print summary
    print

    if not errors:
        visualisation = O.getOutput("visualisation")
        if visualisation :
            for i in range(len(visualisation)) :
                if i and not i % 3 :
                    print
                print visualisation[i]
            #for
            print
        #if

        reference = O.getOutput("reference")[-1]
        for i in O.getOutput("descriptions") :
            print i
        print
        for i in O.getOutput("protDescriptions") :
            print i
        print

        if RD.record and RD.record._sourcetype == "LRG": #LRG record
            from collections import defaultdict
            toutput = defaultdict(list)
            poutput = defaultdict(list)
            for i in RD.record.geneList:
                for j in i.transcriptList:
                    d = j.description
                    d = ';' in d and '['+d+']' or d
                    if j.name:
                        toutput[i.name].append(
                            "%st%s:%c.%s" % (reference, j.name, j.molType, d))
                    else:
                        pass
                    if j.molType == 'c':
                        poutput[i.name].append(
                                "%sp%s:%s" % (reference, j.name,
                                    j.proteinDescription))
                        poutput[i.name].sort()
                toutput[i.name].sort()

            #Transcript Notation
            print "Following transcripts were affected:"
            for key, values in toutput.items():
                print key
                for value in values:
                    print "\t"+value

            #Protein Notation
            print "\nFollowing proteins were affected:"
            for key, values in poutput.items():
                print key
                for value in values:
                    print "\t"+value
            #for
        #if
        else :
            for i in RD.record.geneList :
                for j in i.transcriptList :
                    if ';' in j.description :
                        print "%s(%s_v%s):%c.[%s]" % (reference, i.name, j.name,
                                                      j.molType, j.description)
                    else :
                        print "%s(%s_v%s):%c.%s" % (reference, i.name, j.name,
                                                    j.molType, j.description)
                        if (j.molType == 'c') :
                            print "%s(%s_i%s):%s" % (reference, i.name, j.name,
                                                     j.proteinDescription)
                    #else
                #for
            #for
        #else

        #Genomic Notation
        rdrd = RD.record.description
        gdescr = ';' in rdrd and '['+rdrd+']' or rdrd
        print "\nGenomic notation:\n\t%s:g.%s" % (reference, gdescr)
        print O.getOutput("genomicChromDescription")

        op = O.getOutput("oldprotein")
        if op :
            print "\nOld protein:"
            #__bprint(op[0], O)
            #for i in O.getOutput("oldProteinFancy") :
            #    print i
            print 'Disabled (see how wsgi.py handles this)'
            print
        #if
        np = O.getOutput("newprotein")
        if np :
            print "\nNew protein:"
            #__bprint(np[0], O)
            #for i in O.getOutput("newProteinFancy") :
            #    print i
            print 'Disabled (see how wsgi.py handles this)'
            print
        #if
        ap = O.getOutput("altProtein")
        if ap :
            print "\nAlternative protein using start codon %s:" % \
                O.getOutput("altstart")[0]
            #__bprint(ap[0], O)
            #for i in O.getOutput("altProteinFancy") :
            #    print i
            print 'Disabled (see how wsgi.py handles this)'
            print
        #if

        for i in O.getOutput("exonInfo") :
            print i
        print
        print O.getOutput("cdsStart")
        print O.getOutput("cdsStop")
        print

        for i in O.getOutput("legends") :
            print i

        print
        print "Restriction sites:"
        for i in O.getOutput("restrictionSites") :
            print i

        print "+++ %s" % O.getOutput("myTranscriptDescription")

    #if
    ### OUTPUT BLOCK ###
    del O
#main


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Please provide a variant'
        sys.exit(1)

    # Todo: Fix Mutalyzer to not depend on working directory
    if not os.path.dirname(__file__) or os.path.dirname(__file__) == '.':
        os.chdir('..')
    else:
        root_dir = os.path.split(os.path.dirname(__file__))[0]
        if root_dir:
            os.chdir(root_dir)

    main(sys.argv[1])