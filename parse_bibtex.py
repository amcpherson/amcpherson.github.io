import sys
import pandas
import urlparse
import bibtexparser
import pypandoc
import namedentities


months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec',
]

months_df = pandas.DataFrame({
    'month':months,
    'NUMERIC_MONTH':xrange(len(months))
})

bib_database = bibtexparser.load(sys.stdin)

bib_df = pandas.DataFrame(bib_database.entries)

bib_df = bib_df.merge(months_df, how='outer')

null_month_titles = bib_df.loc[bib_df['NUMERIC_MONTH'].isnull(), 'title'].values
if len(null_month_titles) > 0:
    raise Exception('Invalid month for:\n' + '\n'.join(null_month_titles))

title_order = (bib_df
    .sort(['year', 'NUMERIC_MONTH'], ascending=False)
    .groupby('title', sort=False)
    .first()
    .reset_index()
    ['title']
    .reset_index()
    .rename(columns={'index':'SORT_ORDER'})
)

print '''---
layout: page
title: Publications
---

# Publications

'''

bib_df = bib_df.merge(title_order).sort('SORT_ORDER')

for title, entries in bib_df.groupby('title', sort=False):

    entries = entries.sort('ENTRYTYPE')
    main_entry = entries.iloc[0]

    sys.stdout.write('## ' + main_entry['title'] + '\n')

    write_comma = False
    for author in main_entry['author'].split(' and '):

        if write_comma:
            sys.stdout.write(', ')
        write_comma = True

        author = pypandoc.convert(author, 'html', format='latex')
        author = author.replace('<p>', '').replace('</p>', '')
        author = author.replace('<span>', '').replace('</span>', '')
        author = author.rstrip()

        last, first = author.split(', ')
        first = ''.join([a[0] for a in first.split(' ')])
        author = ' '.join([last, first])
        author = namedentities.numeric_entities(author)

        if last.lower() == 'mcpherson' and first.lower().startswith('a'):
            sys.stdout.write('__{0}__'.format(author))
        else:
            sys.stdout.write('{0}'.format(author))

    sys.stdout.write('  \n')

    for idx, entry in entries.iterrows():

        if entry['ENTRYTYPE'] == 'article':
            pub_text = entry['journal'] + ', ' + entry['month'] + ' ' + entry['year'] + '\n'
        elif entry['ENTRYTYPE'] in ['inproceedings', 'incollection']:
            pub_text = entry['booktitle'] + ' ' + entry['year'] + ', ' + entry['address'] + '\n'

        url = entry['bdsk-url-1']

        sys.stdout.write('[{0}]({1})\n'.format(pub_text, url))

        if 'keyword' in entry and pandas.notnull(entry['keyword']):
            for keyword in entry['keyword'].split('; '):
                html_class = keyword.replace(' ', '_').lower()
                sys.stdout.write('&nbsp; <span class={0}>{1}</span> '.format(html_class, keyword))

        sys.stdout.write('  \n')

    sys.stdout.write('\n')

