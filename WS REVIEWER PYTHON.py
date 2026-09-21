"""
WS101 - Week 02 Quiz: Introduction to HTML & HTML5
Interactive multiple-choice quiz - 100 ITEMS
"""


def run_quiz():
    # Each entry: (question, [option a, option b, option c, option d], correct_letter)
    questions = [
        # ---- Module 1: Introduction to HTML (Pre-HTML5) ----
        ("Who invented HTML in 1989 at CERN?",
         ["John McCarthy", "Sir Tim Berners-Lee", "Brendan Eich", "Håkon Wium Lie"], "b"),

        ("HTML 2.0 was standardized by the IETF through which document?",
         ["RFC 1866", "RFC 1945", "ISO 8879", "W3C HTML4"], "a"),

        ("Which HTML version first introduced tables?",
         ["HTML 1.0", "HTML 2.0", "HTML 3.2", "HTML 4.01"], "c"),

        ("Which standard first enforced the strict separation of structure (HTML) and presentation (CSS)?",
         ["HTML 1.0", "HTML 2.0", "HTML 3.2", "HTML 4.01"], "d"),

        ("Which of the following is a block-level element?",
         ["<span>", "<a>", "<div>", "<img>"], "c"),

        ("Which of the following is an inline element?",
         ["<p>", "<h1>", "<table>", "<span>"], "d"),

        ("What does the browser build when it parses HTML markup?",
         ["CSS Object Model", "Document Object Model", "Server Request Model", "Style Rule Model"], "b"),

        ("In classic HTML 4.01, how was page layout typically structured?",
         ["Using <article> and <section>", "Using generic <div> containers with id/class",
          "Using <header> and <footer>", "Using <canvas>"], "b"),

        ("Which technology was typically required to embed audio/video before HTML5?",
         ["Native <video> tags", "External plugins like Flash or Java applets",
          "<canvas> rendering", "WebSockets"], "b"),

        ("How did the W3C attempt to reform HTML around the year 2000?",
         ["By creating HTML5", "By reformulating HTML 4.01 into XHTML 1.0",
          "By deprecating all attributes", "By introducing the DOM"], "b"),

        ("Which statement about SGML-based HTML is TRUE?",
         ["All tags must be lowercase", "Tags must always be closed explicitly",
          "Tag names are case-insensitive", "Attributes must always be quoted"], "c"),

        ("In XHTML, how must void tags be written?",
         ["<br>", "<br/> (self-closing)", "<BR/> with spaces inside", "They are not allowed"], "b"),

        ("In classic HTML, what was a common misuse of <table> elements?",
         ["Storing database records", "Controlling visual grid layout before CSS positioning",
          "Creating forms", "Embedding video"], "b"),

        ("Which input types were established by HTML 2.0/4.01?",
         ["text, password, checkbox, radio", "email, url, range, color",
          "date, tel, search, number", "canvas, svg, video"], "a"),

        # ---- Module 2: Introduction to HTML5 ----
        ("What is the primary goal of HTML5 regarding media?",
         ["To require Flash for playback", "To enable native video and audio playback",
          "To remove all media support", "To use only Silverlight"], "b"),

        ("Which element defines introductory content or navigational links?",
         ["<section>", "<header>", "<aside>", "<main>"], "b"),

        ("Which element is designed for self-contained content that could be distributed independently?",
         ["<div>", "<aside>", "<article>", "<span>"], "c"),

        ("Which element contains content indirectly related to the main content (like a sidebar)?",
         ["<aside>", "<footer>", "<article>", "<nav>"], "a"),

        ("What attribute on <video> displays playback controls to the user?",
         ["loop", "autoplay", "controls", "poster"], "c"),

        ("Which is NOT an HTML5 input type?",
         ["email", "range", "color", "font"], "d"),

        ("Which attribute provides client-side validation with a regular expression?",
         ["required", "placeholder", "pattern", "autofocus"], "c"),

        ("Which HTML5 feature is a procedural, pixel-based drawing area manipulated by JavaScript?",
         ["Inline SVG", "Canvas API", "Web Storage", "Web Workers"], "b"),

        ("Which HTML5 feature keeps each SVG element in the DOM tree, suited for icons and UI components?",
         ["Canvas", "Inline SVG", "WebSockets", "Geolocation"], "b"),

        ("Which API enables background thread execution so heavy calculations don't freeze the UI?",
         ["WebSockets", "Web Storage", "Web Workers", "Geolocation"], "c"),

        ("Which API replaces cookies for local data with persistent and tab-scoped options?",
         ["Web Storage", "Geolocation", "Drag and Drop", "WebSockets"], "a"),

        ("What capacity does HTML5 localStorage typically offer per domain?",
         ["4 KB", "40 KB", "5MB+", "500MB"], "c"),

        ("Which API opens a persistent two-way channel ideal for chat and live feeds?",
         ["Web Workers", "WebSockets", "Geolocation", "Drag and Drop"], "b"),

        ("How does the HTML5 doctype differ from HTML4's?",
         ["It is longer and more complex", "It requires an SGML reference",
          "It is simply <!DOCTYPE html>", "It was removed entirely"], "c"),

        ("In HTML5, the Geolocation API requires:",
         ["Automatic access to user coordinates", "User permission",
          "A CSS stylesheet", "An external plugin"], "b"),

        ("Which element specifies the dominant content of the body?",
         ["<main>", "<section>", "<div>", "<article>"], "a"),

        ("Which element encloses major navigation links?",
         ["<header>", "<nav>", "<main>", "<aside>"], "b"),

        ("<section> represents:",
         ["Self-contained content", "A standalone section of functionality or topic",
          "Navigation links", "Secondary content"], "b"),

        ("<footer> defines:",
         ["Introductory content", "The footer for a section or page",
          "The main content", "A sidebar"], "b"),

        ("Which HTML5 revision replaced outdated plugins like Flash or Silverlight?",
         ["HTML 3.2", "HTML 4.01", "XHTML 1.0", "HTML5"], "d"),

        # ---- Module 3: HTML Structure ----
        ("What does the DOM represent?",
         ["A CSS file", "A tree-like map built by the browser from HTML",
          "A server protocol", "An image format"], "b"),

        ("In the DOM, every HTML tag, attribute, and text piece becomes a:",
         ["Class", "Node", "File", "Cache entry"], "b"),

        ("What is the top of the DOM tree called?",
         ["<html>", "document", "<body>", "<head>"], "b"),

        ("What is the purpose of <!DOCTYPE html>?",
         ["To add a title", "To link CSS",
          "To render the page in Standard Mode (not Quirks Mode)", "To define the charset"], "c"),

        ("Is <!doctype html> valid?",
         ["No, DOCTYPE must be uppercase only", "Yes, the declaration is case-insensitive",
          "Only with an SGML reference", "Only in XHTML"], "b"),

        ("What does lang=\"en\" on the <html> element declare?",
         ["The character encoding", "The primary human language of the document",
          "The browser version", "The CSS language"], "b"),

        ("Which meta tag configures mobile responsiveness?",
         ["<meta charset=\"UTF-8\">",
          "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
          "<meta name=\"description\">", "<link rel=\"icon\">"], "b"),

        ("How many bytes must the charset declaration appear within?",
         ["First 512 bytes", "First 1024 bytes", "First 2048 bytes", "Anywhere in the document"], "b"),

        ("Where does the <title> text appear?",
         ["Only in the page body", "In the visible content area only",
          "In browser tabs, bookmarks, and search results", "In the CSS file"], "c"),

        ("What does the DOM API let JavaScript do?",
         ["Only read the page", "Change the page in real time without reloading",
          "Replace the browser", "Only store data"], "b"),

        ("In the HTML5 document skeleton, which contains the user-visible content?",
         ["<head>", "<body>", "<meta>", "<!DOCTYPE>"], "b"),

        ("Why do we need the DOM?",
         ["HTML is static and cannot react on its own", "To encrypt the page",
          "To replace CSS", "To speed up the server"], "a"),

        ("The <head> element contains:",
         ["User-visible content", "Non-visual metadata and resource links",
          "Only images", "Only paragraphs"], "b"),

        ("Why is the DOM called a live tree?",
         ["It reloads every second", "JavaScript can edit it without reloading the page",
          "It only exists offline", "It is stored in cookies"], "b"),

        # ---- Module 4: Elements, Tags, and Attributes ----
        ("What is a tag?",
         ["A complete content unit", "A property inside an opening tag",
          "A marker enclosed in angle brackets", "A file path"], "c"),

        ("What is an attribute?",
         ["A marker inside angle brackets", "A modifier inside an opening tag (name=\"value\")",
          "The text content of an element", "A closing marker"], "b"),

        ("What is an element?",
         ["Only the opening tag", "The complete structure: opening tag, attributes, content, closing tag",
          "Only the content", "Only the closing tag"], "b"),

        ("Which is a self-closing (void) tag?",
         ["<p>", "<img>", "<div>", "<h1>"], "b"),

        ("Which of these is a paired tag pair?",
         ["<img>", "<br>", "<a> and </a>", "<hr>"], "c"),

        ("Which type of attribute is applicable to almost any tag (id, class, style)?",
         ["Element-specific", "Boolean", "Global", "Void"], "c"),

        ("Which attribute is element-specific to <img>?",
         ["href", "src", "type", "pattern"], "b"),

        ("Which is a Boolean attribute?",
         ["href", "disabled", "src", "title"], "b"),

        ("What does alt on <img> provide?",
         ["A tooltip", "The file source", "Alternative text for accessibility", "Image dimensions"], "c"),

        ("Which is an inline element?",
         ["<div>", "<h1>", "<strong>", "<p>"], "c"),

        ("Which is a block-level element?",
         ["<span>", "<section>", "<a>", "<em>"], "b"),

        ("In <ul id=\"shopping-list\"><li>Apples</li></ul>, what is <li> called relative to <ul>?",
         ["A sibling", "A parent", "A nested/child element", "An attribute"], "c"),

        ("What does class=\"btn primary\" demonstrate?",
         ["A Boolean attribute", "A single class only", "Multiple reusable CSS classes", "A unique ID"], "c"),
    ]

    # ---- Module 5 & 6 continuation (assembled below) ----
    questions += [
        ("Which heading represents the highest level?",
         ["<h6>", "<h1>", "<h3>", "<head>"], "b"),

        ("How should heading levels be chosen?",
         ["Based on font size", "Based on document structure/hierarchy",
          "Randomly", "Based on color"], "b"),

        ("Which is the main heading of a page?",
         ["<h2>", "<h3>", "<h1>", "<h6>"], "c"),

        ("What does <p> represent?",
         ["A page", "A paragraph of text", "A panel", "Presentation"], "b"),

        ("What happens to whitespace in HTML source code?",
         ["All spaces render exactly as typed", "Consecutive whitespace collapses into a single rendered space",
          "Whitespace is deleted entirely", "Whitespace creates new paragraphs"], "b"),

        ("What does <br> do?",
         ["Creates a thematic break", "Inserts a line break within content",
          "Creates a paragraph", "Adds bold text"], "b"),

        ("What kind of element is <br>?",
         ["Paired", "Void", "Block-level", "Semantic container"], "b"),

        ("When should <br> be used?",
         ["For page layout spacing", "When a line break is part of the content (e.g., an address)",
          "To make text larger", "To create paragraphs"], "b"),

        ("<strong> indicates:",
         ["Stylistic bold only", "Strong importance/seriousness/urgency",
          "Italic emphasis", "Highlighted text"], "b"),

        ("<em> represents:",
         ["Emphasis", "Deletion", "Insertion", "Superscript"], "a"),

        ("Which element draws attention WITHOUT indicating strong importance?",
         ["<strong>", "<b>", "<em>", "<mark>"], "b"),

        ("<i> is used for:",
         ["Just italic styling, no semantic purpose",
          "Text in an alternate voice/mood (technical term, foreign phrase)",
          "Important warnings only", "Highlighted text"], "b"),

        ("<mark> indicates:",
         ["Deleted content", "Highlighted/relevant text", "Small print", "Inserted content"], "b"),

        ("Which element is best for fine print or side comments?",
         ["<small>", "<big>", "<sup>", "<del>"], "a"),

        ("<del> represents:",
         ["Inserted content", "Deleted content (strikethrough)",
          "Emphasized content", "Highlighted content"], "b"),

        ("<ins> represents:",
         ["Deleted content", "Inserted content (underlined)", "Subscript", "Bold text"], "b"),

        ("How is water written using <sub>?",
         ["H<sup>2</sup>O", "H<sub>2</sub>O", "H<mark>2</mark>O", "H<del>2</del>O"], "b"),

        ("Which element represents 2<sup>10</sup> (superscript)?",
         ["<sub>", "<sup>", "<ins>", "<em>"], "b"),

        ("<hr> represents:",
         ["A horizontal decorative image", "A thematic break between sections",
          "A line break within a paragraph", "A header section"], "b"),

        ("Which is a common beginner mistake?",
         ["Using <h1> for the main title", "Using headings just to make text bigger",
          "Using <p> for paragraphs", "Using <strong> for warnings"], "b"),

        ("What is the better approach to make a paragraph look large?",
         ["Use <h3> for it", "Use CSS with a class", "Use <br> many times", "Use <strong>"], "b"),

        ("In the hierarchy H1 -> H2 -> H3, which correctly shows a subsection under H2?",
         ["<h3> under <h2>", "<h1> under <h2>", "<h6> directly under <h1>, skipping levels",
          "Any heading at any level"], "a"),

        ("Which heading levels are used most commonly on ordinary pages?",
         ["<h1>, <h2>, <h3>", "<h4>, <h5>, <h6>", "Only <h1>", "Only <h6>"], "a"),

        ("Which syntax creates an HTML comment?",
         ["// comment", "/* comment */", "<!-- comment -->", "# comment"], "c"),

        ("Does an HTML comment appear on the rendered webpage?",
         ["Yes, always", "No, the browser ignores it", "Only in the <head>",
          "Only if it contains text"], "b"),

        ("HTML comments are primarily intended for:",
         ["Users viewing the page", "Developers reading the source",
          "Search engines only", "CSS parsing"], "b"),

        ("Can comments temporarily disable HTML code?",
         ["No, they are display-only", "Yes, commented elements won't appear",
          "Only in the <head>", "Only with JavaScript"], "b"),

        ("Which is a BAD use of HTML comments?",
         ["Identifying sections", "Explaining why code exists",
          "Storing passwords and API keys", "Leaving reminders"], "c"),

        ("Why is putting passwords in comments dangerous?",
         ["It slows the page", "Users can view the HTML source with developer tools",
          "The browser crashes", "It removes the doctype"], "b"),

        ("What does whitespace in HTML source refer to?",
         ["Only spaces", "Only tabs", "Spaces, tabs, line breaks, and indentation",
          "Only blank lines"], "c"),

        ("What is the primary purpose of whitespace and indentation?",
         ["Making the browser load faster", "Source-code readability and maintainability",
          "Encrypting HTML", "Replacing CSS"], "b"),

        ("What is the common indentation convention recommended in the module?",
         ["8 spaces per level", "4 spaces per level (2 also acceptable)",
          "1 tab always", "No indentation"], "b"),

        ("What is the most important rule regarding indentation?",
         ["Always use 4 spaces", "Consistency", "Always use tabs", "Never indent"], "b"),

        ("What does good indentation communicate?",
         ["The color of elements", "The parent-child relationship between elements",
          "The file size", "The page title"], "b"),

        ("Which element is intended for the primary content of a webpage?",
         ["<content>", "<body>", "<main>", "<article>"], "c"),

        ("Which semantic element describes a thematic section of content?",
         ["<div>", "<section>", "<span>", "<nav>"], "b"),

        ("What is \"proper nesting\"?",
         ["Elements opened anywhere and closed anywhere",
          "Elements opened inside a parent should close inside that same parent",
          "Closing all tags at the start", "Never closing tags"], "b"),

        ("Which is the best example of organized HTML?",
         ["<section><h2>About</h2><p>Welcome</p></section> (one line)",
          "Multi-line with indentation of nested elements",
          "Improperly closed tags", "All tags on one line"], "b"),

        ("Which practice is generally recommended?",
         ["Put all HTML on one line", "Use random indentation",
          "Use meaningful comments and consistent indentation", "Avoid semantic elements"], "c"),

        ("Which is NOT one of the three basic good practices taught in Module 6?",
         ["Comments", "Whitespace", "Code organization", "Hiding code from users"], "d"),

        ("A well-organized HTML5 document commonly follows:",
         ["HEAD with metadata, title, CSS references; BODY with header, nav, main, footer",
          "All content in <head>", "Body first, then head", "No structure"], "a"),

        ("What does &copy; produce?",
         ["The word \"copy\"", "The (c) copyright symbol", "A comment", "A paragraph"], "b"),

        ("Which is a poor beginner practice highlighted in the module?",
         ["Using comments to identify sections", "Using <br> repeatedly for page layout spacing",
          "Indenting nested elements", "Using <main> for primary content"], "b"),
    ]

    total = len(questions)
    score = 0
    wrong = []

    print("=" * 55)
    print("  WS101 - WEEK 02 QUIZ: Introduction to HTML & HTML5")
    print("=" * 55)
    print(f"  {total} questions. Type a, b, c, or d. Good luck!\n")

    for i, (question, options, answer) in enumerate(questions, start=1):
        print(f"Q{i}. {question}")
        labels = ["a", "b", "c", "d"]
        for label, option in zip(labels, options):
            print(f"   {label}) {option}")

        while True:
            choice = input("Your answer: ").strip().lower()
            if choice in labels:
                break
            print("   Invalid input. Please type a, b, c, or d.")

        if choice == answer:
            score += 1
            print("   Correct!\n")
        else:
            wrong.append(i)
            print(f"   Wrong. The correct answer is {answer}.\n")

    percentage = round((score / total) * 100, 2)

    print("=" * 55)
    print("                    RESULTS")
    print("=" * 55)
    print(f"  Score:      {score} / {total}")
    print(f"  Percentage: {percentage}%")

    if wrong:
        print(f"  Missed:     {', '.join('Q' + str(n) for n in wrong)}")
    else:
        print("  Missed:     None - perfect score!")

    if percentage >= 90:
        remark = "Excellent! You've mastered this module."
    elif percentage >= 75:
        remark = "Good job! Review the missed items to polish up."
    elif percentage >= 60:
        remark = "Fair. Reread the modules and try again."
    else:
        remark = "Needs improvement. Please revisit the entire module."

    print(f"  Remark:     {remark}")
    print("=" * 55)


if __name__ == "__main__":
    run_quiz()
