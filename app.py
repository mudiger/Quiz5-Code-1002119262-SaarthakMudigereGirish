from flask import request
from flask import Flask
from flask import render_template
import os
import passlib.pwd

from bs4 import BeautifulSoup
from pprint import pprint
import PyPDF2, nltk, requests, io
import regex as re
from collections import defaultdict
from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.stem import snowball
from nltk.corpus import stopwords

# nltk.download_shell()
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


def extract_words_from_pdf(file_path):
    # response = requests.get(file_path)
    # pdf_content = response.content
    #
    # pdf_stream = io.BytesIO(pdf_content)
    # reader = PyPDF2.PdfReader(pdf_stream)
    response = requests.get(file_path)
    text = response.text
    words = []
    sentences = []
    # for page in text:
    #     # page
    #     text = page.extract_text()
    #     # sentences
    for sent in sent_tokenize(text):
        # words
        sentences.append(sent)
        word_tokens = word_tokenize(sent)
        words += word_tokens
    return sentences, words


# sentences = sent_tokenize(' '.join(words_list))
# Specify the path to your PDF file
pdf_file_path = r'https://storageaccount1002119262.blob.core.windows.net/assignment5-blob-1002119262-saarthakmudigeregirish/Textbook3.txt'
# Call the function to extract words from the PDF
words_list = extract_words_from_pdf(pdf_file_path)


@app.route("/")
def index():
    return render_template("index.html")

'''
@app.route("/page1/", methods=['GET', 'POST'])
def page1():



    def validate_password(password):
        policy = passlib.pwd.PasswordPolicy.from_names(
            length=8,
            uppercase=2,
            lowercase=1,
            digits=1
        )
    return policy.test(password)

    password = "P@ssw0rd"
    if validate_password(password):
        print("Valid password")
    else:
        print("Invalid password")
    return render_template("1)Page.html")

'''
@app.route("/page2/", methods=['GET', 'POST'])
def page2():
    count_list = []
    full_text = ''
    if request.method == "POST":
        text = request.form['text']

        # initializing tag
        tag = ["b","i","h1","p"]
        texts=[]
        for i in tag:
            # regex to extract required strings
            reg_str = "<" + i + ">(.*?)</" + i + ">"
            texts.append(re.findall(reg_str, text))
        # soup = BeautifulSoup(text, 'html.parser')
        # texts = [*soup.stripped_strings]
        # print(texts)

        clean = re.compile('<.*?>')
        print(clean)
        full_text = re.sub(clean, '', text)
        re.findall(r'<b>.*(\[|\]).*</b>', text)

    return render_template("2)Page.html", full_text=full_text, texts=texts)

'''
@app.route("/page3/", methods=['GET', 'POST'])
def page3():
    # convert them all to lower case and eliminate duplicates
    lower_corpus_words = set([ x.lower() for x in words_list[1]])

    replaced = []
    if request.method == "POST":
        old_char = request.form['chars']
        new_char = request.form['replace']

        modified_tokens = [token.replace(old_char, new_char) for token in words_list[1]]
        modified_contents = ' '.join(modified_tokens)

        # Print the top few lines
        num_lines_to_print = 8  # Specify the number of lines to print
        lines = modified_contents.split('. ')  # Split the modified contents into lines
        for line in lines[:num_lines_to_print]:
            replaced.append(('============>', line))
        # # Write the modified contents back to the file
        # with open(pdf_file_path, 'w') as file:
        #     file.write(modified_contents)

    return render_template("3)Page.html", replaced=replaced)


@app.route("/page4/", methods=['GET', 'POST'])
def page4():
    w_in_s = []

    if request.method == "POST":
        n = int(request.form['n'])
        word = request.form['word']

        def search_word_in_sentence(w, s, f):
            tokens = nltk.word_tokenize(s)
            if w in tokens and f>0:
                w_in_s.append(('============>', s))
                return f - 1  # Decrement n by 1 and return the updated value
            return f  # Return n unchanged if the condition is not met

        c = n
        for sentence in words_list[0]:
            c = search_word_in_sentence(word, sentence, c)
            if c == 0:
                break

    return render_template("4)Page.html", w_in_s=w_in_s)

'''
if __name__ == "__main__":
    app.run(debug=True)


# # This will contain a list of all words in the corpus
# corpus_words = []
#
# # Tokenize a paragraph into sentences and each sentence in to
# # words
# for c in corpus:
#     for sent in sent_tokenize(c):
#         word_tokens = word_tokenize(sent)
#         corpus_words += word_tokens
#
# print(len(corpus_words))
#
# # convert them all to lower case and eliminate duplicates
# lower_corpus_words = set([ x.lower() for x in corpus_words ])
# print(len(lower_corpus_words))
#
#
# # Remove the stopwords
# from nltk.corpus import stopwords
#
# stwords = set(stopwords.words('english'))
#
# # Using set difference to eliminate stopwords from our words
# stopfree_words = lower_corpus_words - stwords
# len(stopfree_words)
#
# # grammar tense
# stemmer = snowball.SnowballStemmer('english')
# stemmed_words = set([stemmer.stem(x) for x in stopfree_words])
# print(stemmed_words)
#
#
# # Our index is a map of word -> documents it is found in
# inverted_index = defaultdict(set)
#
# # We maintain the reference to the document by its index in the corpus list
# for docid, c in enumerate(corpus):
#     for sent in sent_tokenize(c):
#         for word in word_tokenize(sent):
#             word_lower = word.lower()
#             if word_lower not in stwords:
#                 word_stem = stemmer.stem(word_lower)
#                 # We add the document to the set againt the word in our
#                 # index
#                 inverted_index[word_stem].add(docid)
#
# print(sorted(inverted_index.keys()))
#
#
# def process_and_search(query):
#     matched_documents = set()
#     for word in word_tokenize(query):
#         word_lower = word.lower()
#         if word_lower not in stwords:
#             word_stem = stemmer.stem(word_lower)
#             matches = inverted_index.get(word_stem)
#             if matches:
#                 # The operator |= is a short hand for set union
#                 matched_documents |= matches
#     return matched_documents
#
# print(len(process_and_search("alice")))