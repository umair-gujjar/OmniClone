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

        if filename == 'actions.txt':
            all_data = []
            for a in actions:
                action_data = []
                for d in [a.comment, a.completed, a.dateAdded, a.dateChanged, a.deferUntil, a.displayIndex, a.due, a.estTime, a.flagged, a.project, a.status, a.tags, a.title]:
                    action_data.append(d)
                all_data.append(action_data)
            json.dump(all_data, fp)
            
        elif filename == 'events.txt':
            all_data = []
            for e in events:
                event_data = []
                for d in [e.comment, e.dateStart, e.dateEnd, e.project, e.tags, e.title]:
                    event_data.append(d)
                all_data.append(event_data)
            json.dump(all_data, fp)
        
        elif filename == 'inbox.txt':
            all_data = []
            for i in inbox:
                inbox_data = []
                for d in [i.comment, i.completed, i.dateAdded, i.dateChanged, i.deferUntil, i.displayIndex, i.due, i.estTime, i.flagged, i.project, i.status, i.tags, i.title]:
                    inbox_data.append(d)
                all_data.append(inbox_data)
            json.dump(all_data, fp)
            
        elif filename == 'projects.txt':
            all_data = []
            for p in projects:
                project_data = []
                for d in [p.comment, p.completed, p.dateAdded, p.dateChanged, p.deferUntil, p.displayIndex, p.due, p.estTime, p.flagged, p.status, p.tags, p.title]:
                    project_data.append(d)
                all_data.append(project_data)
            json.dump(all_data, fp)
            
        elif filename == 'tags.txt':
            json.dump(tags)
            
        else:
            print('ERROR in saves.py: Wrong \'filename\' passed to list_to_file()')



def file_to_list(filename):
    with open(filename, 'r') as fp:
        if filename == ''
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
