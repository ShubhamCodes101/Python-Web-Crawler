import os


# creating folder for each new website to be crawled
def create_folder(directory):
    if not os.path.exists(directory):
        print("Generating project folder : " + directory)
        os.makedirs(directory)
    else:
        print("Project folder already exists !!!")


# create queue for waiting links and crawled links
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        # helper function to create and write links to files
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# creating write_file function
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# appending links in file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# deleting contents from file
def delete_from_file(path ):
    with open(path, 'w'):
        pass

# adding file contents(each link) to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results

# adding set items to file
def set_to_file(links, file_name):
    delete_from_file(file_name)
    for link in sorted(links):
        append_to_file(file_name, link)

#create_folder('thenewboston')
#create_data_files("thenewboston", "https://thenewboston.com")