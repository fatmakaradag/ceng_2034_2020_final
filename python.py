#!/ usr/ bin/ python3
import os,requests,uuid,sys
from multiprocessing import Process
import multiprocessing,hashlib


print('parent proc PID:',os.getpid())        #PID always has randomly variable.
child=os.fork()
if child==0:
   print('child PID:',os.getpid())          #PID always has randomly variable.
  
   os._exit(0)
  
print('here is parent proc')



url=[
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg"]

#def download_url():
#    for url in a:
#        url=requests.get("i")
#        url.status_code
#        with open("url.jpg","wb")as f:
#            f.write(url.content)
#            f.close()
        
#processes = []                               hocam bu kodda hata vermiyor ama neden indirmedi anlayamadim.
#                                                bu calismami da gormeniz icin silmedim.              

#for i in range(multiprocessing.cpu_count()):
#     processes.append(Process(target=download_url,))
     
#for process in processes:
#    process.start()
#for process in processes:
 #   process.join()
 
def download_file(url,file_name=None):
     r=requests.get(url,allow_redirects=True)
     file=file_name if file_name else str(uuid.uuid4())
     open(file,'wb').write(r.content)
     
for i in url:
     download_file(i,file_name=None)
     
     
os.wait() #Both the parent process and the child process competes for the CPU with all other processes in the system. The operating systems decides which process to execute when and for how long. The process in the system execute concurrently.The wait system call blocks the caller until one of its child process terminates. If the caller doesn’t have any child processes, wait returns immediately without blocking the caller. Using wait the parent can obtain the exit status of the terminated child.Thus, children work and finish first, then work on the parent.    
     
     


    

'''
b = []
def url_duplicate():
   
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
          filehash = hashlib.md5(open(filename, "rb").read()).hexdigest()
          if filehash not in b:
            b.append(filehash)
          else:
            print(b)
'''
files = []
file_names = []
def url_duplicates(dir):
    for filename in os.listdir(dir):
        if os.path.isfile(filename):
          file_names.append(filename)
          filehash = hashlib.md5(open(filename, "rb").read()).hexdigest()
          files.append(filehash)
url_duplicates(os.getcwd())

duplicates = []
unique = []
indexes = []
index = 0
def find_duplicates(array):
  for i in files:
    global index
    if i not in unique:
        unique.append(i)
    else:
        duplicates.append(i)
        print(file_names[index])
        indexes.append(index)
    index += 1

print("Duplicate files: ")
find_duplicates(files)
print("Hexadecimal format of the duplicate files: ")
print(duplicates)

'''          #It finds duplicates but when it is done with the process it prints four times so I got the process part in the comment.
processes = []           
for i in range(multiprocessing.cpu_count()):
    processes.append(Process(target=find_duplicates, args=(files,)))
     
for process in processes:
    process.start()
for process in processes:
    process.join()

''' 

 
'''   
def chunk_reader(fobj, chunk_size=5):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hashobj = hash()
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hashobj.update(chunk)
                file_id = (hashobj.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)
                if duplicate:
                    print ("Duplicate found: %s and %s" % (full_path, duplicate))
                else:
                    hashes[file_id] = full_path

if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])
else:
    print ("Please pass the paths to check as parameters to the script")
    
    
    
for i in url:
    check_for_duplicates("/home/fatma")

'''















  
