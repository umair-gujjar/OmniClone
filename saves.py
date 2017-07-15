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
            print('ERROR in saves.py: Wrong \'filename\' passed to list_to_file() method')



def file_to_list(filename):

    with open(filename, 'r') as fp:

        if filename == 'actions.txt':

            all_data = json.load(fp)
            global actions
            actions = []

            for d in all_data:

                a = ocObjects.Action()

                a.comment       = d[0]
                a.completed     = d[1]
                a.dateAdded     = d[2]
                a.dateChanged   = d[3]
                a.deferUntil    = d[4]
                a.displayIndex  = d[5]
                a.due           = d[6]
                a.estTime       = d[7]
                a.flagged       = d[8]
                a.project       = d[9]
                a.status        = d[10]
                a.tags          = d[11]
                a.title         = d[12]

                actions.append(a)


        elif filename == 'events.txt':

            all_data = json.load(fp)
            global events
            events = []

            for d in all_data:
                a = ocObjects.Event()

                e.comment       = d[0]
                e.dateStart     = d[1]
                e.dateEnd       = d[2]
                e.project       = d[3]
                e.tags          = d[4]
                e.title         = d[5]

                actions.append(a)


        elif filename == 'inbox.txt':

            all_data = json.load(fp)
            global inbox
            inbox = []

            for d in all_data:
                a = ocObjects.Action()

                a.comment = d[0]
                a.completed = d[1]
                a.dateAdded = d[2]
                a.dateChanged = d[3]
                a.deferUntil = d[4]
                a.displayIndex = d[5]
                a.due = d[6]
                a.estTime = d[7]
                a.flagged = d[8]
                a.project = d[9]
                a.status = d[10]
                a.tags = d[11]
                a.title = d[12]

                inbox.append(a)


        elif filename == 'projects.txt':

            all_data = json.load(fp)
            global projects
            projects = []

            for d in all_data:

                p = ocObjects.Project()

                p.comment       = d[0]
                p.completed     = d[1]
                p.dateAdded     = d[2]
                p.dateChanged   = d[3]
                p.deferUntil    = d[4]
                p.displayIndex  = d[5]
                p.due           = d[6]
                p.estTime       = d[7]
                p.flagged       = d[8]
                p.status        = d[9]
                p.tags          = d[10]
                p.title         = d[11]

                projects.append(p)


        elif filename == 'tags.txt':

            global tags
            tags = json.load(fp)


        else:
            print('ERROR in saves.py: Wrong \'filename\' passed to file_to_list() method')


print(projects)
file_to_list('projects.txt')
"""
p1 = ocObjects.Project()
p1.title = 'p1'
projects.append(p1)
p2 = ocObjects.Project()
p2.title = 'p2'
projects.append(p2)
p3 = ocObjects.Project()
p3.title = 'p3'
projects.append(p3)
p4 = ocObjects.Project()
p4.title = 'p4'
projects.append(p4)

list_to_file('projects.txt')"""
print(projects)
