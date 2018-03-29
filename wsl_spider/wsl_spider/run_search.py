# Run this file to parse a list of returned course page.
import sys
import getopt
from scrapy import cmdline


def format_arg(arg, str_base):
    return ["-a"] + [str_base.format(arg)] if arg else []


def parse_cmd_options():
    # Displayed language: en or jp
    display_lang = ""
    # These two schools return little course results and are good for testing:
    # art_architecture, sports_sci
    # Target schools:
    # sils, poli_sci, fund_sci_eng, cre_sci_eng, adv_sci_eng
    schools = ""
    # Language which the course is taught in: all, en, jp, or n/a (don't recommend the last option)
    teaching_lang = ""
    # Target keywords: IPSE, English-based Undergraduate Program
    keyword = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:d:t:k:')
    except getopt.GetoptError:
        print("Usage: python3 run_search.py -d display_language -s school_one,school_two " +
              "-t teaching_language -k a_single_keyword")
        sys.exit(2)

    for o, a in opts:
        if o == '-d':
            display_lang = a
        elif o == '-s':
            schools = a
        elif o == '-t':
            teaching_lang = a
        elif o == '-k':
            keyword = a
        else:
            assert False, "unhandled option"

    display_lang_arg = format_arg(display_lang, "display_lang={}")
    schools_arg = format_arg(schools, "schools={}")
    teaching_lang_arg = format_arg(teaching_lang, "teaching_lang={}")
    keyword_arg = format_arg(keyword, "keyword={}")

    return display_lang_arg + schools_arg + teaching_lang_arg + keyword_arg


command = "scrapy crawl search"
# print(command.split() + parse_cmd_options())
cmdline.execute(command.split() + parse_cmd_options())
