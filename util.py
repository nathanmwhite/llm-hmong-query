prompt_prefix = """Please translate the following words from Hmong to English: \
miv - cat, \
lig - late, \
pov - throw, \
khob - cup, \
dav - wide, \
nce - ascend, \
tsheb - car, \
ntxov - early, \
hiab - weave, \
toj - hill, \
da dej - bathe, \
faib - share, \
xeeb ntxwv - grandchildren, \
pib - start, \
hniav - tooth, \
ntxuav - wash, \
ntiaj teb - world, \
soj ntsuam - investigate, \
kua mis - milk, \
txias - cool, \
xiav - blue, \
cob qhia - instruct, \
vwj - crazy, \
dais - bear, \
lwj - spoiled, \
nyeem - read,"""

words = {'ua': ['make', 'do'],
         'los': 'come',
         'tau': 'get',
         'hais': 'say',
         'muaj': 'have',
         'rau': ['insert', 'put', 'put in'],
         'mus': 'go',
         'zoo': 'good',
         'Hmoob': 'Hmong',
         'nyob': ['live', 'stay'],
         'tuaj': 'come',
         'neeg': 'person',
         'kev': 'way',
         'paub': 'know',
         'xav': ['want', 'think'],
         'muab': ['take', 'grab'],
         'txog': ['arrive', 'about'],
         'lus': ['speech', 'language', 'word'],
         'siab': ['liver', 'heart', 'high'],
         'teb': ['answer', 'field'],
         'luag': ['other', 'others', 'laugh'],
         'coj': ['take', 'lead'],
         'pab': ['help', 'group'],
         'saib': ['look at', 'watch'],
         'txiv': ['father', 'husband', 'fruit'],
         'pom': 'see',
         'me': ['little', 'small'],
         'ntau': 'many',
         'noj': 'eat',
         'niam': ['mother', 'wife', 'woman'],
         'tub': ['son', 'child'],
         'tom': ['bite', 'there', 'on that side'],
         'rov': 'return',
         'qab': ['back', 'sweet'],
         'hnub': 'day',
         'neej': 'life',
         'tuag': 'die',
         'tawm': ['go out', 'exit'],
         'tham': ['talk', 'chat'],
         'ntawv': ['book', 'paper'],
         'dab': 'spirit',
         'tsev': 'house',
         'cia': ['leave', 'let'],
         'tso': ['put', 'leave', 'first'],
         'tua': ['shoot', 'kill'],
         'heev': ['strong', 'very'],
         'siv': 'use',
         'kawm': ['learn', 'study'],
         'txawj': ['leader', 'smart', 'skilled', 'good at', 'know'],
         'nyiaj': 'money',
         'sawv': ['stand up', 'get up', 'stand'],
         'ntseeg': 'believe',
         'qhia': ['teach', 'tell'],
         'tseeb': 'true',
         'tsuas': ['only', 'dark'],
         'ntuj': 'sky',
         'xyoo': 'year',
         'coob': 'many',
         'muag': ['sell', 'eye'],
         'tshaj': 'exceed',
         'kwv': ['brother', 'younger brother'],
         'Nplog': 'Lao',
         'laus': 'old',
         'hu': ['call', 'sing'],
         'sau': ['write', 'gather'],
         'tes': 'hand',
         'dua': ['tear', 'pass', 'surpass'],
         'loj': ['big', 'large'],
         'txhua': ['every', 'enough'],
         'poj': ['woman', 'grandmother'],
         'zog': 'strength',
         'cai': ['law', 'rule'],
         'hlub': 'love',
         'sim': ['try', 'lifetime'],
         'hluas': 'young',
         'zaum': ['time', 'sit'],
         'yug': ['be born', 'born', 'bear'],
         'tswv': ['lord', 'master', 'leader', 'chief'],
         'npe': 'name',
         'ntxiv': ['add', 'more'],
         'hnov': ['hear', 'feel'],
         'npaum': ['be equal', 'equal', 'like'],
         'phem': 'bad',
         'nkauj': ['young woman', 'song'],
         'thov': ['beg', 'ask', 'please'],
         'ntej': ['before', 'in front', 'front'],
         'dhau': 'surpass',
         'dag': ['joke', 'lie'],
         'ntshai': ['be afraid', 'afraid', 'fear', 'maybe'],
         'koom': 'meet',
         'nom': ['leader', 'chief'],
         'raws': ['in accordance with', 'like'],
         'ntse': ['sharp', 'smart'],
         'tseg': ['throw away', 'abandon'],
         'chaw': 'place',
         'nyiam': 'like',
         'suav': ['count', 'Chinese'],
         'txaus': 'enough',
         'ntev': 'long',
         'xeem': ['surname', 'last name'],
        }
