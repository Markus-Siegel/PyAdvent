from fpdf import FPDF
import os

advent_calendar = [
    "Bei einer Kerze ist nicht das Wachs wichtig, sondern das Licht.", 
    "Ein frommer Zauber hält mich wieder, anbetend, staunend muss ich stehn; es sinkt auf meine Augenlider ein gold'ner Kindertraum hernieder, ich fühl's - ein Wunder ist geschehn.", 
    "Es treibt der Wind im Winterwalde\ndie Flockenherde wie ein Hirt\nund manche Tanne ahnt wie balde\nsie fromm und lichterheilig wird.\nUnd lauscht hinaus: den weißen Wegen\nstreckt sie die Zweige hin - bereit\nund wehrt dem Wind und wächst entgegen\nder einen Nacht der Herrlichkeit.", 
    "Ich lag und schlief; da träumte mir\nein wunderschöner Traum:\nEs stand auf unserm Tisch vor mir\nein hoher Weihnachtsbaum.\n\n\nUnd bunte Lichter ohne Zahl,\ndie brannten ringsumher;\ndie Zweige waren allzumal\nvon goldnen Äpfeln schwer. ", 
    "Die meisten Menschen bringen so das ganze Leben hin, dass sie sich von Pfingsten nach Weihnachten und von Weihnachten wieder nach Pfingsten sehnen.", 
    "O Weihnacht! Weihnacht! Höchste Feier! Wir fassen ihre Wonne nicht. Sie hüllt in ihre heilgen Schleier das seligste Geheimnis dicht.", 
    "Von drauss' vom Walde komm ich her;\nIch muss euch sagen, es weihnachtet sehr!\n\n\nAllüberall auf den Tannenspitzen\nsah ich goldene Lichtlein sitzen;\n\n\nUnd droben aus dem Himmelstor\nsah mit grossen Augen das Christkind hervor;", 
    "Ihr Kinder, sperrt die Näschen auf,\nEs riecht nach Weihnachtstorten;\nKnecht Ruprecht steht am Himmelsherd\nUnd bäckt die feinsten Sorten.\n\n\nIhr Kinder, sperrt die Augen auf,\nSonst nehmt den Operngucker:\nDie große Himmelsbüchse, seht,\nTut Ruprecht ganz voll Zucker.", 
    "Wo die Zweige am dichtesten hangen,\ndie Wege am tiefsten verschneit,\nda ist um die Dämmerzeit\nim Walde das Christkind gegangen.\n\n\nEs mußte sich wacker plagen,\ndenn einen riesigen Sack\nhat's meilenweit huckepack\nauf den schmächtigen Schultern getragen.", 
    "Nicht ein Flügelschlag ging durch die Welt,\nStill und blendend lag der weiße Schnee.\nNicht ein Wölklein hing am Sternenzelt,\nKeine Welle schlug im starren See.\n\n\nAus der Tiefe stieg der Seebaum auf,\nBis sein Wipfel in dem Eis gefror;\nAn den Ästen klomm die Nix herauf,\nSchaute durch das grüne Eis empor.", 
    "Von den Tannen träufelt Märchenduft;\nLeise Weihnachtsglocken sind erklungen -\nBlinkend fährt mein Hammer durch die Luft;\nDenn ein Spielzeug zimmr' ich meinem Jungen.\n\n\nGraue Wolken kämpfen fernen Kampf;\nBlau darüber strahlt ein harter Himmel.\nDurch die Nüstern stößt den weißen Dampf\nVor der Tür des Nachbars breiter Schimmel.", 
    "Durch den Flockenfall\nklingt süßer Glockenschall,\nist in der Winternacht\nein süßer Mund erwacht.\n\n\nHerz, was zitterst du\nden süßen Glocken zu?\nWas rührt den tiefen Grund\ndir auf der süße Mund?", 
    "Welch lustiger Wald um das hohe Schloß\nhat sich zusammengefunden,\nEin grünes bewegliches Nadelgehölz,\nVon keiner Wurzel gebunden!\n\n\nAnstatt der warmen Sonne scheint\nDas Rauschgold durch die Wipfel;\nHier backt man Kuchen, dort brät man Wurst,\nDas Räuchlein zieht um die Gipfel.", 
    "Vom Himmel in die tiefsten Klüfte\nEin milder Stern herniederlacht.\nVom Tannenwalde steigen Düfte\nUnd hauchen durch die Winterlüfte,\nUnd kerzenhelle wird die Nacht.\n\n\nMir ist das Herz so froh erschrocken,\nDas ist die liebe Weihnachtszeit!\nIch höre fernher Kirchenglocken\nMich lieblich heimatlich verlocken\nIn märchenstille Herrlichkeit.", 
    "Weißer Rauhreif auf den Bäumen\nund der Schnee lädt ein zum Träumen,\ndie Äste glitzern frostbizarr\nund der See glänzt kälteklar,\ndie Sonne strahlt in sattem Blau\ndes Himmels und wohin ich schau',\nerblick ich Schnee am Waldesrand,\noh, du Winterwunderland.", 
    "Alles still! es tanzt den Reigen\nMondenstrahl in Wald und Flur,\nUnd darüber thront das Schweigen\nUnd der Winterhimmel nur.\n\n\nAlles still! vergeblich lauschet\nMan der Krähe heisrem Schrei.\nKeiner Fichte Wipfel rauschet,\nUnd kein Bächlein summt vorbei. ", 
    "Wie schön geschmückt der festliche Raum!\nDie Lichter funkeln am Weihnachtsbaum!\nO fröhliche Zeit! O seliger Traum!\n\n\nDie Mutter sitzt in der Kinder Kreis;\nnun schweiget alles auf ihr Geheiß:\nsie singet des Christkinds Lob und Preis.", 
    "Es war einmal eine Glocke,\ndie machte baum, baum.\nUnd es war einmal eine Flocke,\ndie fiel dazu wie im Traum.\n\n\nDie fiel dazu wie im Traum....\nDie sank so leis hernieder\nwie ein Stück Engleingefieder\naus dem silbernen Sternenraum.", 
    "Gesegnet sei die heilige Nacht,\ndie uns das Licht der Welt gebracht! -\n\n\nWohl unterm lieben Himmelszelt\ndie Hirten lagen auf dem Feld.\n\n\nEin Engel Gottes, licht und klar,\nmit seinem Gruß tritt auf sie dar...", 
    "Markt und Strassen steh'n verlassen,\nStill erleuchtet jedes Haus,\nSinnend geh' ich durch die Gassen,\nAlles sieht so festlich aus.\n\n\nAn den Fenstern haben Frauen\nBuntes Spielzeug fromm gechmückt,\nTausend Kindlein steh'n und schauen,\nSind so wunderstill beglückt.", 
    "Das Christkind aber möge euch bringen\ndie schönsten von allen schönen Dingen,\nund was ihr nur immer träumt, wünscht, oder dachtet,\ndass ihr es wohl gerne haben möchtet.", 
    "Bäume leuchtend, Bäume blendend,\nÜberall das Süße spendend,\nIn dem Ganzen sich bewegend,\nAlt- und junges Herz erregend -\nSolch ein Fest ist uns bescheret,\nMancher Gaben Schmuck verehret;\nStaunend schaun wir auf und nieder,\nHin und her und immer wieder.", 
    "Und so leuchtet die Welt langsam der Weihnacht entgegen und der in Händen sie hält, weiß um den Segen.", 
    "Die Sonne weicht dem Licht der Sterne,\ndas zärtlich Stadt und Land erhellt.\nUnd hoffnungsvoll sind nah und ferne\ndie Menschen auf der ganzen Welt.\n\n\nEin Wunsch entsteigt dem Schein der Kerzen\ndie flackernd auf dem Christbaum glühn:\nEs möge doch in alle Herzen\ndie Sehnsucht nach dem Frieden ziehn.", 
    ]

advent_calendar_authors = [
    "Antoine de Saint-Exupéry", 
    "Theodor Storm", 
    "Rainer Maria Rilke", 
    "August Heinrich Hoffmann von Fallersleben", 
    "Theodor Fontane", 
    "Nikolaus Lenau", 
    "Theodor Storm", 
    "Paula Dehmel", 
    "Anna Ritter", 
    "Gottfried Keller", 
    "Otto Ernst Schmidt", 
    "Gustav Falke", 
    "Gottfried Keller", 
    "Theodor Storm", 
    "Oskar Stock", 
    "Theodor Fontane", 
    "Peter Cornelius", 
    "Christian Morgenstern", 
    "Eduard Mörike", 
    "Joseph Freiherr von Eichendorff", 
    "Wilhelm Busch", 
    "Johann Wolfgang von Goethe", 
    "Matthias Claudius", 
    "Poldi Lembcke", 
    ]

# Create a document in A5 landscape.
pdf = FPDF("L", "mm", format="A5")
pdf.set_author("Markus Siegel");
pdf.set_title("Adventskalendar");

pdf.add_page()
pdf.set_font("Courier", "B", 30)
# Print the document headline.
pdf.cell(0, 50, "Adventskalendar", 0, 0, "C")

# Add a page for each day until Christmas.
for i in range(24):
    # Each day gets its own page.
    pdf.add_page()

    # Setup the font for the day text.
    pdf.set_font("Courier", "B", 40)
    # Gold color.
    pdf.set_text_color(225, 185, 100)

    # Add one because we start at zero. But we need to start at zero for accessing the lists.
    day = str(i + 1)

    # Print the day with a border.
    pdf.cell(25, 25, day, 1, 1, "C")
    pdf.ln(10)

    # Setup the font for the quote.
    pdf.set_font("Courier", "", 16)
    pdf.set_text_color(50, 50, 50)

    # Print the quote for the day.
    pdf.multi_cell(0, 5, advent_calendar[i])
    pdf.ln(10)

    # Setup the font for the author.
    pdf.set_font("Courier", "I", 16)
    pdf.set_text_color(120, 120, 120)

    # Print the author of the quote.
    pdf.cell(0, 5, "- " + advent_calendar_authors[i] + " -", 0, 0, "R")
    pdf.ln()

# Generate the pdf file.
filename = "Adventskalendar.pdf"
pdf.output(filename)
