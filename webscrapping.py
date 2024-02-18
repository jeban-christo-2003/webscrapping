#!/usr/bin/env python
# coding: utf-8

# In[84]:


from bs4 import BeautifulSoup as bs
import requests


# In[91]:


url="https://www.mygreatlearning.com/academy/learn-for-free/courses/data-science-foundations"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
soup.prettify()


# In[92]:



# Find the first 'p' tag
table = soup.find("p")

# Find all 'p' tags and extract their text
p_tags = soup.find_all('p')
for tag in p_tags:
    print(tag.get_text())


# In[54]:



csv_filename = "scraped_data.csv"

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the text data to the CSV file
    for text in text_data:
        csv_writer.writerow([text])

print(f"Data has been saved to {csv_filename}")


# In[71]:


import json

# Create a JSON object (dictionary)
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize (convert to JSON string)
json_string = json.dumps(person)

# Deserialize (convert JSON string to a Python dictionary)
person_copy = json.loads(json_string)

print("Original Person:", person)
print("Serialized JSON:", json_string)
print("Deserialized Person:", person_copy)


# In[ ]:




