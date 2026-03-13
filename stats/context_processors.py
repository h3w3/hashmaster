# my_app/context_processors.py
import hashmaster

def project_version(request):
    return {
        'APP_VERSION': hashmaster.__version__,
        'APP_KENNEL': hashmaster.__kennel__,
        'APP_LOGO': hashmaster.__logo__,
        'APP_HOMEPAGE': hashmaster.__homepage__,
        'APP_SLOGAN': hashmaster.__slogan__,
    }
