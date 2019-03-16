import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db.models import Q
import logging
import traceback
from inia.models import Dataset
from inia.analysis.intersect import hypergeometric_score, format_hypergeometric_score, bonferroni_factor
from itertools import combinations

_LOG = logging.getLogger('application.'+__name__)
TEMPLATE_FILE_LOCATION = os.path.join(settings.PROJECT_DIR, 'proj', 'inia', 'templates', '_dataset_matrix.html')

class Command(BaseCommand):
    help = 'Uses the database calculate intersection statistics between all datasets.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        '''
        This command should generate a parital view for the existing datasets by calculating the theoretical intersections
        between each set.  We cache this information rather than run it every time the page is loaded because it
        can take quite a bit of database load.

        O(n) = N^2

        User generated datasets are then just utilized on an as-needed basis.

        After calculating hypergeoemtric socre, you need to adjust it with bonferroni.
        my $bonferroni = scalar(@datasets) * (scalar(@datasets) - 1) / 2;
        adjustment = hypergeometricscore * bonferroni.
        Then take the minn... has tto be <= 1...
        $hypScoreAdj = min(1, $hypScore * $bonferroni);

        '''
    try:
        html = '{# This file is automatically generated by generate_dataset_matrix.  Run that command to generate this ' \
                'for now datasets. #}\n\n'
        data_sets = Dataset.objects.all().prefetch_related('iniagene_set').order_by('name')

        bonferroni_adjustment = bonferroni_factor()

        combinations = combinations(data_sets, 2)
        html += '<tr>'
        html += '<td class="col-name">'
        html += '-'  #  First column needs first row to be blank to make table align correctly.
        html += '</td>'
        # header
        for ds in data_sets:
            html += '<td class="col-name">'
            html += ds.name
            html += '</td>'
        html += '</tr>'

        # Data...
        for ds in data_sets:
            html += '<tr>'
            html += '<td>'
            html += ds.name
            html += '</td>'
        # maybe can't utilize combinations... since we need table output... investigate further.
            for ds2 in data_sets:
                html += '<td>'
                if ds == ds2:
                    html += '-'
                else:
                    score = hypergeometric_score(ds, ds2)
                    score = score * bonferroni_adjustment  # adjust it
                    score = min(1, score)  # Cna't be > 1.  if > set =1
                    if score <= 0.05:
                        html += '<mark>'
                    html += format_hypergeometric_score(score)
                    if score <= 0.05:
                        html += '</mark>'
                html += '</td>'
            html += '</tr>'



        with open(TEMPLATE_FILE_LOCATION, 'w') as file:
            file.write(html)


    except:
        _LOG.error("Exception:")
        _LOG.error(traceback.format_exc())
