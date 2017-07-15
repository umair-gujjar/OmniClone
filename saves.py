import json
import ocObjects

projects    = []
actions     = []
events      = []
inbox       = []
tags        = []


def list_to_file(filename):
    with open(filename, 'r+') as fp:
        fp.truncate()
        if filename == 'projects.txt':
            all_data = []
            for p in projects:
                project_data = []
                for d in [p.comment, p.completed, p.dateAdded, p.dateChanged, p.deferUntil, p.displayIndex, p.due, p.estTime, p.flagged, p.status, p.tags, p.title]:
                    project_data.append(d)
                all_data.append(project_data)
            json.dump(all_data, fp)
        else:
            None


def file_to_list(filename):
    with open(filename, 'r') as fp:
        a = json.load(fp)
    print(a)



p1 = ocObjects.Project()
p1.title = 'p1'
projects.append(p1)
p2 = ocObjects.Project()
p2.title = 'p2'
projects.append(p2)

#list_to_file('projects.txt')

file_to_list('projects.txt')
