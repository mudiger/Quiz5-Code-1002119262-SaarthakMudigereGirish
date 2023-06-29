from flask import request
from flask import Flask
from flask import render_template
import os
import regex as re

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route("/")
def index():
    return render_template("index.html")

'''
@app.route("/page1/", methods=['GET', 'POST'])
def page1():
    def validate_password(password, vf):
        L1, L2, IV = vf
        if len(password) < L1 or len(password) > L2:
            return "NotValid: Password length should be between {} and {} characters.".format(L1, L2)

        if not any(char.isdigit() for char in password):
            return "NotValid: Password should contain at least one digit."

        if sum(1 for char in password if char.isupper()) < 2:
            return "NotValid: Password should contain at least two uppercase letters."

        if not any(char in '#@+-%' for char in password):
            return "NotValid: Password should contain at least one of the characters: #@+-%."

        if any(char in '!@$*' for char in password):
            return "NotValid: Password should not contain the characters: {!@$*}."

        if any(char in IV for char in password):
            return "NotValid: Password should not contain the characters specified in the 'IV' list."

        return "Valid"

    # Admin enters the valid form (VF)
    L1 = int(input("Enter the minimum password length: "))
    L2 = int(input("Enter the maximum password length: "))
    IV = input("Enter additional characters to exclude (IV): ")

    vf = (L1, L2, IV)

    # User enters the password to check (CP)
    password = input("Enter the password to check: ")

    # Validate the password
    result = validate_password(password, vf)
    print(result)


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