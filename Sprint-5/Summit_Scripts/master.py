import os
    
output_path = '/projects/sebr8260/Summit_Scripts'

files_to_run = []
for folder in os.listdir(output_path):
    if folder != '.DS_Store' and folder != '.ipynb_checkpoints' and folder != 'sample_scripts' and folder.split('.')[0] != 'master' and folder.split('-')[0] != 'sample' and folder.split('-')[0] != 'slurm' and folder != 'create_pairs.ipynb':
        for shfile in os.listdir(os.path.join(output_path, os.path.join(folder, 'shell_files'))):
            if shfile != '.ipynb_checkpoints':
                files_to_run.append('/projects/sebr8260/Summit_Scripts/{}/shell_files/{}'.format(shfile.split('.')[0].split('_')[0], shfile))

for file in files_to_run:
    os.system('sbatch {}'.format(file))

