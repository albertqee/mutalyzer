"""
Default Mutalyzer settings. Override these with settings in the module
pointed-to by the `MUTALYZER_SETTINGS` environment variable.
"""


# Todo: Find an alternative to the temporary directories/files defined here,
#   since they are created even if the setting is reset from another
#   configuration file, and they are never removed.


# Use Mutalyzer in debug mode.
DEBUG = False

# We are running unit tests.
TESTING = False

# This address is used in contact information on the website, as sender in
# batch job notifications, and with retrieval of records at the NCBI using
# Entrez.
EMAIL = 'mutalyzer@humgen.nl'

# The cache directory. Used to store uploaded and downloaded files (e.g.,
# reference files from NCBI or user) and batch job results.
import tempfile
CACHE_DIR = tempfile.mkdtemp()

# Maximum size of the cache directory (in bytes).
MAX_CACHE_SIZE = 50 * 1048576 # 50 MB

# Maximum size for uploaded and downloaded files (in bytes).
MAX_FILE_SIZE = 10 * 1048576 # 10 MB

# Redis connection URI (can be any redis-py connection URI). Set to `None` to
# silently use a mock Redis. Redis is only used for non-essential features.
REDIS_URI = None

# Database connection URI (can be any SQLAlchemy connection URI).
DATABASE_URI = 'sqlite://'

# Default genome assembly (by name or alias).
DEFAULT_ASSEMBLY = 'hg19'

# Name and location of the log file.
import os
import tempfile
log_handle, log_filename = tempfile.mkstemp()
os.close(log_handle)
LOG_FILE = log_filename

# Level of logged messages.
LOG_LEVEL = 3

# Level of output messages.
OUTPUT_LEVEL = 1

# Format of time prefix for log messages. Can be anything that is accepted as
# the format argument of time.strftime.
# http://docs.python.org/2/library/time.html#time.strftime
LOG_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Prefix URL from where LRG files are fetched.
#LRG_PREFIX_URL = 'ftp://ftp.ebi.ac.uk/pub/databases/lrgex/'
LRG_PREFIX_URL = 'ftp://ftp.ebi.ac.uk/pub/databases/lrgex/SCHEMA_1_7_ARCHIVE/'

# Allow for this fraction of errors in batch jobs.
BATCH_JOBS_ERROR_THRESHOLD = 0.05

# Expiration time for transcript->protein links from the NCBI (in seconds).
PROTEIN_LINK_EXPIRATION = 60 * 60 * 24 * 30

# Expiration time for negative transcript->protein links from the NCBI (in
# seconds).
NEGATIVE_PROTEIN_LINK_EXPIRATION = 60 * 60 * 24 * 5

# URL to the SOAP webservice WSDL document. Used for linking to it from the
# documentation page on the website.
SOAP_WSDL_URL = 'https://mutalyzer.nl/services/?wsdl'

# URL to the HTTP/RPC+JSON webservice root (without trailing slash). Used for
# linking to it from the documentation page on the website.
JSON_ROOT_URL = 'https://mutalyzer.nl/json'

# Is Piwik enabled?
PIWIK = False

# Base URL for the Piwik server.
PIWIK_BASE_URL = 'https://piwik.example.com'

# Piwik site ID for Mutalyzer.
PIWIK_SITE_ID = 1
