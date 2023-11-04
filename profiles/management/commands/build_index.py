from django.core.management.base import BaseCommand

from profiles.documents import ElapsedTimeDocument, ProfileDocumentManager, ElaspedTimeDocumentManager, ELASTICSEARCH_ENABLED


# TODO параметризация
class Command(BaseCommand):
    help = 'build search index'

    def handle(self, *args, **options):
        if ELASTICSEARCH_ENABLED:
            ElaspedTimeDocumentManager.build_index()
            manager = ElapsedTimeDocument()
            manager.init()
            manager = ProfileDocumentManager()
            manager.delete_index()
            manager.rebuild()