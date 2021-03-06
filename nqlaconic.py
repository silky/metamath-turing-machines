import nqlgrammar
import nqlast
import argparse

parser = argparse.ArgumentParser(description="Compiles Not-Quite-Laconic descriptions to Turing machines and executes them.")
parser.add_argument('nql_file', help='NQL file to read')
parser.add_argument('--print-ast', action='store_true', \
    help='Print the parsed AST')
parser.add_argument('--print-tm', action='store_true', \
    help='Print the generated turing machine states')
parser.add_argument('--print-subs', action='store_true', \
    help='Print the generated subprogram objects')
parser.add_argument('--run-tm', action='store_true', \
    help='Run the turing machine')
parser.add_argument('--dont-compress', action='store_true', \
    help='Keep indistinguishable states')
parser.add_argument('--no-cfg-optimize', action='store_true', \
    help='Disable control-flow optimizer')
parser.add_argument('--relative-jumps', action='store_true', \
    help='Use additively relative jumps')
args = parser.parse_args()

ast, = nqlgrammar.grammar.parseFile(args.nql_file, parseAll=True)

if args.print_ast:
    print(repr(ast))
else:
    nqlast.harness(ast, args)