import pandas as pd
import re

tsv_file = input('Enter absolute source file path: ')
csv_table = pd.read_table(tsv_file)
source_data = pd.DataFrame(csv_table,
                           columns=csv_table.columns.values)

split_sample_ids = []
rows_having_taxonomic_profile = []
species_with_taxonomic_profile = []
final_rows = []

rows = [csv_table.columns.values]

for index, row in source_data.iterrows():
    rows.append(row.values)
    split_sample_ids.append(str(row['#SampleID']).split('|'))

for i in range(len(split_sample_ids)):

    for j in range(len(split_sample_ids[i])):

        sample_id_values = split_sample_ids[i][j]
        taxonomic_profiles = re.search('^t__', sample_id_values)

        if taxonomic_profiles:

            rows_having_taxonomic_profile.append(split_sample_ids[i])
            sample_id_with_taxonomic_profile = str(split_sample_ids[i])
            raw_specie_name = re.search('s__(.+),', sample_id_with_taxonomic_profile)

            if raw_specie_name:
                found = raw_specie_name.group()
                species_name = found.split('__')[1].split("'")[0]  # cleaned specie name extracted here

                species_with_taxonomic_profile.append(species_name)
                rows[i + 1][0] = str(species_name)
                final_rows.append(rows[i + 1])

df = pd.DataFrame(final_rows)

df.columns = df.iloc[0]
df = df[0:]
df.columns = csv_table.columns.values
df = df.iloc[:, 0:]

total = 0
for i in range(1, len(rows[0])):
    total += df[rows[0][i]]
df['Aggregate'] = total
dataframe_to_export = pd.DataFrame(df, columns=['#SampleID', 'Aggregate'])
dataframe_to_export.to_csv(input('Enter absolute output file path: '), index=False)
