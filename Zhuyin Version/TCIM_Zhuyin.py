KEYS = (
    '特',
    'ㄅ-', 'ㄆ-', 'ㄇ-', 'ㄈ-', '變-', 'ㄧ-', 'ㄨ-', 'ㄚ-', 'ㄜ-', 'ㄯ-', 'ㆭ-', '異-',
    '-ㄅ', '-ㄆ', '-ㄇ', '-ㄈ', '-變', '-ㄧ', '-ㄨ', '-ㄚ', '-ㄜ', '-ㄯ', '-ㆭ', '-異',
)

IMPLICIT_HYPHEN_KEYS = ()

SUFFIX_KEYS = ()

NUMBER_KEY = '特'

NUMBERS = {
    'ㄯ-': '1-',
    'ㄚ-': '2-',
    'ㄧ-': '3-',
    'ㄇ-': '4-',
    'ㄅ-': '5-',
    '-ㄅ': '-6',
    '-ㄇ': '-7',
    '-ㄧ': '-8',
    '-ㄚ': '-9',
    '-ㄯ': '-0',
}

UNDO_STROKE_STENO = '變-變'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        '特': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),

        'ㄯ-': 'q',
        'ㆭ-': 'a',
        'ㄚ-': 'w',
        'ㄜ-': 's',
        'ㄧ-': 'e',
        'ㄨ-': 'd',
        'ㄇ-': 'r',
        'ㄈ-': 'f',
        'ㄅ-': 't',
        'ㄆ-': 'g',
        '異-': 'c',
        '變-': 'v',

        '-變': 'n',
        '-異': 'm',
        '-ㄅ': 'y',
        '-ㄆ': 'h',
        '-ㄇ': 'u',
        '-ㄈ': 'j',
        '-ㄧ': 'i',
        '-ㄨ': 'k',
        '-ㄚ': 'o',
        '-ㄜ': 'l',
        '-ㄯ': 'p',
        '-ㆭ': ';',

        'arpeggiate': 'space',
        'no-op': ('b'),
    },
    'Gemini PR': {
        '特': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),

        'ㄯ-': 'S1-',
        'ㆭ-': 'S2-',
        'ㄚ-': 'T-',
        'ㄜ-': 'K-',
        'ㄧ-': 'P-',
        'ㄨ-': 'W-',
        'ㄇ-': 'H-',
        'ㄈ-': 'R-',
        'ㄅ-': '*1',
        'ㄆ-': '*2',
        '異-': 'A-',
        '變-': 'O-',

        '-變': '-E',
        '-異': '-U',
        '-ㄅ': '*3',
        '-ㄆ': '*4',
        '-ㄇ': '-F',
        '-ㄈ': '-R',
        '-ㄧ': '-P',
        '-ㄨ': '-B',
        '-ㄚ': '-L',
        '-ㄜ': '-G',
        '-ㄯ': '-T',
        '-ㆭ': '-S',

        'no-op': ('-D','-Z','res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = None
DEFAULT_DICTIONARIES = (
	
   
)
