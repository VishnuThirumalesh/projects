import csv
import os
import pickle5 as pickle
import google.oauth2.credentials
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    print("in get_authenticated_service")

    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    #  Check if the credentials are invalid or do not exist
    if not credentials or not credentials.valid:
        # Check if the credentials have expired
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_console()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


def get_video_comments(service, **kwargs):
    print("in get comments")

    comments = []
    results = service.commentThreads().list(part="snippet,replies",videoId="9HnKFUNlcfY", maxResults="100").execute()
    if results["nextPageToken"]:
        print(results["nextPageToken"])
        print("yes")
    kk = 0
    while results:

        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            tokens = re.sub('\[[^]]*\]', '', comment)
            pattern=r'[^a-zA-z0-9\s]'
            tokens=re.sub(pattern,'',tokens)
            # tokens = tokens.split();    
            # print(comment)
            # print(tokens)
            comments.append(tokens)
        try:
            pageT = str(results["nextPageToken"])
            print(pageT)
        
            # comments.append(tokens)
            results = service.commentThreads().list(part="snippet,replies",videoId="9HnKFUNlcfY",pageToken=pageT, maxResults="100").execute()
        except:
            break
  


    return comments

def extractDigits(lst): 
    res = [] 
    for el in lst: 
        sub = el.split(', ') 
        res.append(sub) 
      
    return(res) 

def write_to_csv(comments):
    print("in write_to_csv")
    for i in comments:
        print(i)
    with open('listfile.txt', 'w') as filehandle:
        for listitem in comments:
            filehandle.write('%s\n' % listitem)
 


def get_videos(service, **kwargs):
    print("in get videos")
    final_results = []
    results = service.search().list(**kwargs).execute()

    i = 0
    max_pages = 1
    while results and i < max_pages:
        final_results.extend(results['items'])

        # Check if another page exists
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = service.search().list(**kwargs).execute()
            i += 1
        else:
            break
    print(final_results)        
    return final_results


def search_videos_by_keyword(service, **kwargs):
    print("in search_videos_by_keyword")

    results = get_videos(service, **kwargs)
    
    v = 1
    final_result = []
    for item in results:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        comments = get_video_comments(service, part='snippet', videoId=video_id, textFormat='plainText')
        
        final_result.extend([(video_id, title, comment) for comment in comments]) 
        
        
        v+=1
        break
    write_to_csv(final_result)


if __name__ == '__main__':
    
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    
    
    comments = get_video_comments(service, part='snippet', videoId='9HnKFUNlcfY', textFormat='plainText')
    
    write_to_csv(comments)

