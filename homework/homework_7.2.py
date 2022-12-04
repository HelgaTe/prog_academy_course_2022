"""
Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери).
Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту.
Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
aaaaaaa - Вовочка писав слово - "a"
ititititit - Вовочка писав слово - "it"
catcatcatcat - Вовочка писав слово - "cat"
"""
text = 'olgaolgaolgaolgaolga'
t = len(text)
rev = text[::-1]


for i in range(t):
    if text[0:i + 1] == rev[0:i + 1][::-1]:
        res = text[0:i+1]
        print(res)
        break

"""
Напишіть програму для очищення тексту від HTML-тегів
"""

sample = """
BASICS</strong></h2>
<div class="image"><img src="../images/000085.jpg" alt="Image" class="calibre3"></div>
<p class="noindent">The Python programming language has a wide range of syntactical constructions, standard library functions, and interactive development environment features. Fortunately, you can ignore most of that; you just need to learn enough to write some handy little programs.</p>
<p class="indent">You will, however, have to learn some basic programming concepts before you can do anything. Like a wizard in training, you might think these concepts seem arcane and tedious, but with some knowledge and practice, you’ll be able to command your computer like a magic wand and perform incredible feats.</p>
<p class="indent">This chapter has a few examples that encourage you to type into the <em class="calibre7">interactive shell</em>, also called the <em class="calibre7">REPL</em> (Read-Evaluate-Print Loop), which lets you run (or <em class="calibre7">execute</em>) Python instructions one at a time and instantly shows you the results. Using the interactive shell is great for learning what basic Python instructions do, so give it a try as you follow along. You’ll remember the things you do much better than the things you only read.</p>
<h3 class="h1" id="calibre_link-90"><strong class="calibre2"><span {http:="" www.idpf.org="" 2007="" ops}type="pagebreak" id="calibre_link-875" class="calibre1"></span>Entering Expressions into the Interactive Shell</strong></h3>
<p class="noindent">You can run the interactive shell by launching the Mu editor, which you should have downloaded when going through the setup instructions in the Preface. On Windows, open the Start menu, type “Mu,” and open the Mu app. On macOS, open your Applications folder and double-click <strong class="calibre4">Mu</strong>. Click the <strong class="calibre4">New</strong> button and save an empty file as <em class="calibre7">blank.py</em>. When you run this blank file by clicking the <strong class="calibre4">Run</strong> button or pressing <small class="calibre11">F5</small>, it will open the interactive shell, which will open as a new pane that opens at the bottom of the Mu editor’s window. You should see a <span class="literal">&gt;&gt;&gt;</span> prompt in the interactive shell.</p>

"""

while '<' in sample:
    start = sample.find('<')
    stop = sample.find('>')
    sample = sample.replace(sample[start:stop + 1], '')
print(sample)