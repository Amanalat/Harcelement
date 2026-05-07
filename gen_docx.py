# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, Cm, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r'C:\Users\ASUS\Documents\Web apps\Wordpress\Harcèlement Croatie\doc_textes_partenaires.docx'

C_GREEN  = RGBColor(0x2a,0x7a,0x50)
C_ORANGE = RGBColor(0xc0,0x90,0x30)
C_RED    = RGBColor(0xc0,0x40,0x30)
C_GREY   = RGBColor(0x66,0x66,0x66)
C_DIM    = RGBColor(0x99,0x99,0x99)
C_LIGHT  = RGBColor(0xaa,0xaa,0xaa)
C_BLUE   = RGBColor(0x2a,0x4a,0x7a)
SPK = {
    'leo':RGBColor(0x1a,0x3a,0x6a),'ines':RGBColor(0x4a,0x1a,0x6a),
    'lucas':RGBColor(0x1a,0x5a,0x28),'jade':RGBColor(0x7a,0x3a,0x00),
    'theo':RGBColor(0x2a,0x4a,0x7a),'marine':RGBColor(0x7a,0x1a,0x4a),
    'kevin':RGBColor(0x55,0x55,0x55),'tante':RGBColor(0x5a,0x35,0x10),
    'clara':RGBColor(0x6a,0x1a,0x2a),'narr':RGBColor(0xaa,0xaa,0xaa),
    'lea':RGBColor(0x44,0x88,0x44),
}
CHOICE_BG  = {'good':'F4FAF7','ok':'FDFAF0','bad':'FDF4F4','neutral':'FAFAFA'}
CHOICE_COL = {'good':C_GREEN,'ok':C_ORANGE,'bad':C_RED,'neutral':C_GREY}
CHOICE_HEX = {'good':'2a7a50','ok':'c09030','bad':'c04030','neutral':'555555'}

def _pPr(p): return p._p.get_or_add_pPr()
def set_spacing(para,before=0,after=80,line=276):
    sp=OxmlElement('w:spacing')
    sp.set(qn('w:before'),str(int(before)))
    sp.set(qn('w:after'),str(int(after)))
    sp.set(qn('w:line'),str(int(line)))
    sp.set(qn('w:lineRule'),'auto')
    _pPr(para).append(sp)
def set_indent(para,left=0,hanging=0):
    ind=OxmlElement('w:ind')
    if left: ind.set(qn('w:left'),str(int(left)))
    if hanging: ind.set(qn('w:hanging'),str(int(hanging)))
    _pPr(para).append(ind)
def left_border(para,color_hex,sz=18):
    pBdr=OxmlElement('w:pBdr'); left=OxmlElement('w:left')
    left.set(qn('w:val'),'single'); left.set(qn('w:sz'),str(sz))
    left.set(qn('w:space'),'4'); left.set(qn('w:color'),color_hex)
    pBdr.append(left); _pPr(para).append(pBdr)
def bottom_border(para,color_hex='cccccc',sz=4):
    pBdr=OxmlElement('w:pBdr'); b=OxmlElement('w:bottom')
    b.set(qn('w:val'),'single'); b.set(qn('w:sz'),str(sz))
    b.set(qn('w:space'),'1'); b.set(qn('w:color'),color_hex)
    pBdr.append(b); _pPr(para).append(pBdr)
def shading(para,fill_hex):
    shd=OxmlElement('w:shd'); shd.set(qn('w:val'),'clear')
    shd.set(qn('w:color'),'auto'); shd.set(qn('w:fill'),fill_hex)
    _pPr(para).append(shd)
def keep_together(para): _pPr(para).append(OxmlElement('w:keepLines'))
def page_break_before(para): _pPr(para).append(OxmlElement('w:pageBreakBefore'))
def add_run(para,text,bold=False,italic=False,color=None,size=None,font=None):
    r=para.add_run(text)
    if bold: r.bold=True
    if italic: r.italic=True
    if color: r.font.color.rgb=color
    if size: r.font.size=Pt(size)
    if font: r.font.name=font
    return r

doc=Document()
for sec in doc.sections:
    sec.page_width=Mm(210); sec.page_height=Mm(297)
    sec.left_margin=Cm(2.5); sec.right_margin=Cm(2.5)
    sec.top_margin=Cm(2.2); sec.bottom_margin=Cm(2.2)
for pp in doc.paragraphs: pp._element.getparent().remove(pp._element)

def p(text='',align=WD_ALIGN_PARAGRAPH.LEFT,before=0,after=80,size=11,
      bold=False,italic=False,color=None,font=None,indent=0,line=276):
    para=doc.add_paragraph(); para.alignment=align
    set_spacing(para,before,after,line)
    if indent: set_indent(para,left=indent)
    if text: add_run(para,text,bold=bold,italic=italic,color=color,size=size,font=font)
    return para

def heading2(text,before=160,after=80):
    para=doc.add_paragraph(); set_spacing(para,before=before,after=after)
    add_run(para,text.upper(),bold=True,size=10,color=RGBColor(0x44,0x44,0x44),font='Arial')
    return para

def heading3(text,before=100,after=60):
    para=doc.add_paragraph(); set_spacing(para,before=before,after=after)
    add_run(para,text,bold=True,size=10,color=C_GREY,font='Arial')
    return para

def part_header(num_text,title_text):
    np=doc.add_paragraph(); page_break_before(np)
    set_spacing(np,before=0,after=40); shading(np,'1a1a1a')
    add_run(np,num_text.upper(),bold=False,size=8,color=RGBColor(0x88,0x88,0x88),font='Arial')
    tp=doc.add_paragraph(); set_spacing(tp,before=0,after=160); shading(tp,'1a1a1a')
    add_run(tp,title_text,bold=False,italic=True,size=17,color=RGBColor(0xf0,0xec,0xe4))

def phase_sep(text):
    para=doc.add_paragraph(); set_spacing(para,before=120,after=80)
    add_run(para,f'- {text} -',italic=True,size=8,color=C_DIM,font='Arial')
    para.alignment=WD_ALIGN_PARAGRAPH.CENTER

def time_sep(text):
    para=doc.add_paragraph(); set_spacing(para,before=80,after=60)
    add_run(para,text,italic=True,size=8.5,color=C_DIM,font='Arial')
    para.alignment=WD_ALIGN_PARAGRAPH.CENTER

def dialogue_line(spk_key,spk_label,text,italic_text=False):
    para=doc.add_paragraph(); set_spacing(para,before=0,after=30,line=276)
    keep_together(para)
    add_run(para,f'{spk_label:<12}',bold=True,size=8.5,
            color=SPK.get(spk_key,RGBColor(0x1a,0x1a,0x1a)),font='Arial Narrow')
    para.add_run('  ').font.size=Pt(8)
    add_run(para,text,italic=italic_text,size=10.5,
            color=C_GREY if italic_text else None)

def choice_block(kind,letter,text,reply=None,indent_left=700):
    para=doc.add_paragraph(); set_spacing(para,before=0,after=30,line=276)
    set_indent(para,left=indent_left); left_border(para,CHOICE_HEX[kind],sz=18)
    shading(para,CHOICE_BG[kind]); keep_together(para)
    if letter: add_run(para,f'{letter}  ',bold=True,size=8.5,color=CHOICE_COL[kind],font='Arial')
    add_run(para,text,size=10.5)
    if reply:
        para.add_run('\n')
        add_run(para,reply,italic=True,size=9,color=C_GREY)

def ending_block(kind,title,*lines):
    tp=doc.add_paragraph(); set_spacing(tp,before=80,after=20)
    set_indent(tp,left=300); left_border(tp,CHOICE_HEX.get(kind,'555555'),sz=24)
    shading(tp,CHOICE_BG.get(kind,'FAFAFA'))
    add_run(tp,title,bold=True,size=10.5,color=CHOICE_COL.get(kind,C_GREY))
    for line in lines:
        lp=doc.add_paragraph(); set_spacing(lp,before=0,after=20)
        set_indent(lp,left=300); left_border(lp,CHOICE_HEX.get(kind,'555555'),sz=24)
        shading(lp,CHOICE_BG.get(kind,'FAFAFA'))
        if line.startswith('«') or line.startswith('"') or line.startswith('-'):
            add_run(lp,line,italic=True,size=10,color=C_GREY)
        else: add_run(lp,line,size=10.5)

def quiz_block(num_text,question,options,correct_idx,explanation):
    tp=doc.add_paragraph(); set_spacing(tp,before=120,after=30)
    set_indent(tp,left=200); shading(tp,'F5F7FA'); left_border(tp,'2a4a7a',sz=8)
    add_run(tp,num_text,bold=True,size=10,color=C_BLUE,font='Arial')
    qp=doc.add_paragraph(); set_spacing(qp,before=0,after=60)
    set_indent(qp,left=200); shading(qp,'F5F7FA'); left_border(qp,'2a4a7a',sz=8)
    add_run(qp,question,size=10.5)
    for i,opt in enumerate(options):
        op=doc.add_paragraph(); set_spacing(op,before=0,after=20)
        set_indent(op,left=600); shading(op,'F5F7FA')
        if i==correct_idx: add_run(op,opt,bold=True,size=10,color=C_GREEN)
        else: add_run(op,opt,size=10)
    ep=doc.add_paragraph(); set_spacing(ep,before=40,after=80)
    set_indent(ep,left=200); shading(ep,'F5F7FA'); left_border(ep,'2a4a7a',sz=8)
    add_run(ep,explanation,italic=True,size=9.5,color=C_GREY)

def recovery_block(aunt_line,good_txt,good_reply,bad_txt,bad_reply):
    hp=doc.add_paragraph(); set_spacing(hp,before=60,after=20)
    set_indent(hp,left=600); left_border(hp,'e0c080',sz=12); shading(hp,'FFFBF0')
    add_run(hp,'Rattrapage possible (si mauvaise réponse) :',italic=True,size=9,
            color=RGBColor(0xa0,0x80,0x30),font='Arial')
    ap=doc.add_paragraph(); set_spacing(ap,before=0,after=20)
    set_indent(ap,left=600); left_border(ap,'e0c080',sz=12); shading(ap,'FFFBF0')
    add_run(ap,'La tante   ',bold=True,size=8.5,color=SPK['tante'],font='Arial Narrow')
    add_run(ap,aunt_line,size=10)
    gp=doc.add_paragraph(); set_spacing(gp,before=0,after=20)
    set_indent(gp,left=600); left_border(gp,CHOICE_HEX['good'],sz=14); shading(gp,CHOICE_BG['good'])
    add_run(gp,'ok  ',bold=True,size=9,color=C_GREEN,font='Arial')
    add_run(gp,good_txt,size=10); gp.add_run('\n')
    add_run(gp,good_reply,italic=True,size=9,color=C_GREY)
    bp=doc.add_paragraph(); set_spacing(bp,before=0,after=80)
    set_indent(bp,left=600); left_border(bp,CHOICE_HEX['bad'],sz=14); shading(bp,CHOICE_BG['bad'])
    add_run(bp,'x   ',bold=True,size=9,color=C_RED,font='Arial')
    add_run(bp,bad_txt,size=10); bp.add_run('\n')
    add_run(bp,bad_reply,italic=True,size=9,color=C_GREY)

def footnote_line(text):
    para=doc.add_paragraph(); set_spacing(para,before=200,after=0)
    para.alignment=WD_ALIGN_PARAGRAPH.CENTER; bottom_border(para,'eeeeee',sz=4)
    add_run(para,text,size=8,color=C_LIGHT,font='Arial')

def bullet(text,indent=300):
    para=doc.add_paragraph(); set_spacing(para,before=0,after=30)
    set_indent(para,left=indent)
    add_run(para,'*  ',bold=True,size=10,color=C_DIM)
    add_run(para,text,size=10.5)

def dm_block(account,time_label,harcel_type,messages):
    header=doc.add_paragraph(); set_spacing(header,before=60,after=10)
    set_indent(header,left=200); left_border(header,'3a4a6a',sz=14); shading(header,'F0F4FA')
    add_run(header,account,bold=True,size=9.5,color=C_BLUE,font='Arial')
    add_run(header,f'  {time_label}',size=8,color=C_DIM,font='Arial')
    if harcel_type:
        add_run(header,f'   [{harcel_type}]',italic=True,size=8,color=C_ORANGE,font='Arial')
    for msg in messages:
        mp=doc.add_paragraph(); set_spacing(mp,before=0,after=8,line=260)
        set_indent(mp,left=400); shading(mp,'F7F9FD')
        add_run(mp,f'"{msg}"',size=9.5)

def lea_line(side,text):
    para=doc.add_paragraph(); set_spacing(para,before=0,after=20,line=276)
    keep_together(para)
    lbl='Léa         ' if side=='lea' else 'Clara       '
    col=SPK['lea'] if side=='lea' else SPK['clara']
    add_run(para,lbl,bold=True,size=8.5,color=col,font='Arial Narrow')
    para.add_run('  ').font.size=Pt(8)
    add_run(para,text,size=10.5)

# ═══════════════════════════════════════════════════════
# COUVERTURE
# ═══════════════════════════════════════════════════════
ey=doc.add_paragraph(); ey.alignment=WD_ALIGN_PARAGRAPH.CENTER
set_spacing(ey,before=560,after=100)
add_run(ey,'Jeu pédagogique sur le cyberharcèlement',size=8,color=C_DIM,font='Arial')

ti=doc.add_paragraph(); ti.alignment=WD_ALIGN_PARAGRAPH.CENTER
set_spacing(ti,before=60,after=60); bottom_border(ti,'1a1a1a',sz=12)
add_run(ti,'Retrouver Clara',italic=True,size=26)

su=doc.add_paragraph(); su.alignment=WD_ALIGN_PARAGRAPH.CENTER
set_spacing(su,before=80,after=40)
add_run(su,'Textes complets - Parties 1, 2, 3 et 4\nDocument à destination des partenaires',
        size=10.5,color=C_GREY)

me=doc.add_paragraph(); me.alignment=WD_ALIGN_PARAGRAPH.CENTER
set_spacing(me,before=40,after=200)
add_run(me,'Version mai 2026  *  Usage interne',size=8,color=C_DIM,font='Arial')

heading2('Présentation générale',before=80,after=60)
p('Retrouver Clara est un jeu pédagogique destiné aux collégiens sur le thème du cyberharcèlement. Le joueur incarne Léo, un ami de Clara (14 ans), qui a disparu du collège. En traversant quatre scènes interactives, le joueur reconstitue ce que Clara a vécu et tente de l\'aider.',
  size=10.5,after=60)
p('Ce document présente l\'intégralité des textes jouables des Parties 1, 2, 3 et 4. Les dialogues sont retranscrits tels qu\'ils apparaissent à l\'écran.',
  size=10.5,after=60)

heading2('Structure du jeu',before=80,after=60)
tbl=doc.add_table(rows=5,cols=3); tbl.style='Table Grid'
for i,txt in enumerate(['Partie','Titre','Mécanique']):
    tbl.rows[0].cells[i].text=txt
    r=tbl.rows[0].cells[i].paragraphs[0].runs[0]
    r.bold=True; r.font.size=Pt(8); r.font.name='Arial'
    r.font.color.rgb=RGBColor(0x44,0x44,0x44)
rows_data=[
    ('1','Téléphone d\'Inès','Dialogue à choix multiples, jauge de confiance'),
    ('2','Instagram de Clara','Exploration du profil, identification de types de harcèlement'),
    ('3','Groupe WhatsApp secret','Lecture d\'un chat de groupe, quiz d\'analyse'),
    ('4','Convaincre Clara','Appel téléphonique, jeu d\'empathie'),
]
for i,(num,tit,mec) in enumerate(rows_data,1):
    row=tbl.rows[i].cells; row[0].text=num; row[1].text=tit; row[2].text=mec
    row[2].paragraphs[0].runs[0].italic=True
    row[2].paragraphs[0].runs[0].font.color.rgb=C_GREY
    for cell in row: cell.paragraphs[0].runs[0].font.size=Pt(10)

note=doc.add_paragraph(); set_spacing(note,before=100,after=0)
add_run(note,'Note de lecture : ',bold=True,size=9.5,color=C_GREY,font='Arial')
add_run(note,'options en vert = favorables, orange = neutres, rouge = défavorables.',
        italic=True,size=9.5,color=C_GREY,font='Arial')
footnote_line('Retrouver Clara - Textes partenaires - Mai 2026')

# ═══════════════════════════════════════════════════════
# PARTIE 1 - Page 1
# ═══════════════════════════════════════════════════════
part_header('Partie 1','Téléphone d\'Inès')
pi=doc.add_paragraph(); set_spacing(pi,before=0,after=120); set_indent(pi,left=200)
left_border(pi,'cccccc',sz=18)
add_run(pi,'Léo appelle Inès, la meilleure amie de Clara, pour tenter d\'en savoir plus sur ce qui lui est arrivé. Le joueur doit faire preuve de sensibilité pour gagner sa confiance. Une jauge visible mesure la relation en temps réel.',
        italic=True,size=9.5,color=C_GREY)

heading2('Ouverture')
dialogue_line('leo','Léo','Inès ?')
dialogue_line('ines','Inès','Oui c\'est qui')
dialogue_line('leo','Léo','C\'est Léo. On est dans la même école que Clara.')
dialogue_line('ines','Inès','Je te connais pas.')
dialogue_line('leo','Léo','Je sais. J\'arrive plus à la joindre depuis plusieurs jours. Je ne la vois plus dans la cour. T\'as eu de ses nouvelles ?')
dialogue_line('ines','Inès','Pourquoi tu me demandes ça à moi')

heading2('Étape 1')
h1=doc.add_paragraph(); set_spacing(h1,before=0,after=80)
add_run(h1,'Note : « Je dois être le plus honnête possible, et le plus sincère - c\'est ma seule chance qu\'elle m\'aide. »',
        italic=True,size=9,color=RGBColor(0x88,0x88,0x88),font='Arial')
ch=doc.add_paragraph(); set_spacing(ch,before=0,after=40); set_indent(ch,left=700)
add_run(ch,'Que répond Léo ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','C','« Je suis inquiet. J\'arrive plus à dormir depuis hier soir. »',
             reply='-> (pas de réplique fixe, la conversation se poursuit)')
choice_block('ok','B','« Je savais pas à qui d\'autre m\'adresser. »')
choice_block('bad','A','« Parce que t\'es son amie. Si quelqu\'un sait quelque chose, c\'est toi. »')

heading2('Étape 2')
dialogue_line('ines','Inès','Tu la connais comment toi, Clara ?')
h2=doc.add_paragraph(); set_spacing(h2,before=0,after=80)
add_run(h2,'Note : « Je la connais depuis quelques années. On se croisait souvent à l\'école. Il faut que je le lui montre. »',
        italic=True,size=9,color=RGBColor(0x88,0x88,0x88),font='Arial')
ch=doc.add_paragraph(); set_spacing(ch,before=0,after=40); set_indent(ch,left=700)
add_run(ch,'Que répond Léo ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','A','« On se croise souvent. Je l\'aimais bien. »')
choice_block('ok','C','« On est dans des classes différentes mais on se parle des fois. »')
choice_block('bad','B','« Pas super bien. Mais j\'ai entendu parler d\'elle ces derniers temps. »')

heading2('Étape 3')
dialogue_line('ines','Inès','Elle répond plus à moi non plus.\nDepuis quelques jours.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Que répond Léo ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','A','« Ça lui arrivait déjà avant ? »')
choice_block('ok','C','« Vous vous parliez souvent ? »')
choice_block('bad','B','« Peut-être qu\'elle vous a bloqués. »')

heading2('Étape 4')
dialogue_line('ines','Inès','Non. Jamais.\nÇa faisait un moment qu\'elle était pas bien.\nDepuis le mois dernier au moins.\nElle manquait des cours. Elle répondait plus aux messages.\nElle disait que c\'était rien.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Que répond Léo ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','A','« Tu sais ce qui s\'est passé ? »')
choice_block('ok','C','« Elle avait l\'air d\'avoir peur de quelque chose ? »')
choice_block('bad','B','« Et t\'as pas essayé d\'en parler avec elle ? »')

heading2('Étape 5')
dialogue_line('ines','Inès','Si j\'ai essayé.\nElle voulait pas.\nMais je voyais bien.\nElle laissait son téléphone retourné sur la table. Elle regardait plus ses applis.\nDes fois je lui envoyais un message, je voyais qu\'elle l\'avait lu... et elle répondait pas pendant des heures.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Que répond Léo ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','A','« On dirait qu\'elle voulait s\'éloigner de son téléphone. »')
choice_block('ok','B','« C\'est bizarre comme comportement. »')
choice_block('bad','C','« C\'est peut-être juste une mauvaise période. »')

heading2('Étape 6')
dialogue_line('ines','Inès','Je sais pas si je devrais te raconter tout ça.\nJe te connais même pas.')
h6=doc.add_paragraph(); set_spacing(h6,before=0,after=80)
add_run(h6,'Note : « Elle a raison de se méfier. Je dois la rassurer sans la brusquer. »',
        italic=True,size=9,color=RGBColor(0x88,0x88,0x88),font='Arial')
ch=doc.add_paragraph(); set_spacing(ch,before=0,after=40); set_indent(ch,left=700)
add_run(ch,'Que répond Léo ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','A','« T\'es obligée à rien. C\'est toi qui décides. »')
choice_block('ok','C','« Je veux juste savoir si elle va bien. Rien d\'autre. »')
choice_block('bad','B','« Dis-moi juste ce que tu sais. »')
footnote_line('Retrouver Clara - Partie 1 : Téléphone d\'Inès - Textes partenaires')

# PARTIE 1 - Page 2
part_header('Partie 1 - suite','Crise de confiance & Fins')
h2c=doc.add_paragraph(); set_spacing(h2c,before=0,after=80)
add_run(h2c,'SCÈNE DE CRISE  ',bold=True,size=10,color=RGBColor(0x44,0x44,0x44),font='Arial')
add_run(h2c,'(déclenchée si la confiance chute trop bas)',italic=True,size=10,color=C_LIGHT)
dialogue_line('ines','Inès','Attends.\nT\'es dans quelle classe ?\nTu connais qui dans la sienne ?')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Comment réagit Léo ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','A','« T\'as raison d\'être méfiante. Tu me connais pas. »  (+2)')
choice_block('ok','B','« Je fais pas partie des gens qui lui ont fait du mal. »  (+1)')
choice_block('bad','C','« Fais-moi confiance, j\'essaie juste d\'aider. »  (-1)')

heading2('Fin - Confiance perdue')
dialogue_line('ines','Inès','Arrête de me parler.\nJe te répondrai plus.')
dialogue_line('narr','Système','(elle ne répond plus)',italic_text=True)
ending_block('bad','Rouge - Échec',
    'Inès : « Non. Arrête de fouiller. C\'est pas tes affaires. »',
    '(elle ne répond plus)')

heading2('Fin - Succès fragile')
dialogue_line('ines','Inès','Je sais vraiment pas si je fais bien.\nTu me promets de faire attention ?')
dialogue_line('leo','Léo','Oui.')
dialogue_line('ines','Inès','Tu promets de respecter la vie privée de Clara ?')
dialogue_line('leo','Léo','Oui.')
dialogue_line('ines','Inès','Elle me l\'avait donné au cas où. Tu l\'utilises, t\'en parles à personne.')
ending_block('ok','Jaune - Succès fragile',
    'Inès transmet les identifiants Instagram de Clara.',
    'Compte : @clara.fontaine  -  Mot de passe : nuit_rouge17',
    '« Sois prudent. »')

heading2('Fin - Confiance totale')
dialogue_line('ines','Inès','Tu promets de faire attention à ce que tu lis ?')
dialogue_line('leo','Léo','Je promets.')
dialogue_line('ines','Inès','Et tu me dis si tu trouves quelque chose.')
dialogue_line('ines','Inès','Tu promets de respecter la vie privée de Clara ?')
dialogue_line('leo','Léo','Je le promets.')
dialogue_line('ines','Inès','Elle me l\'avait donné au cas où. Tu l\'utilises, t\'en parles à personne.')
ending_block('good','Vert - Inès te fait confiance',
    'Inès transmet les identifiants Instagram de Clara.',
    'Compte : @clara.fontaine  -  Mot de passe : nuit_rouge17',
    '« C\'est sa vie privée. Respecte-la. »')

heading2('Deuxième conversation (après la Partie 3)',before=120)
p('Visible uniquement si le joueur revient consulter Inès après avoir terminé la Partie 3. La conversation se déroule dans le même téléphone, via une notification discrète.',
  italic=True,size=9.5,color=C_GREY,after=80)
dialogue_line('leo','Léo','Inès, j\'ai peut-être trouvé quelque chose.')
dialogue_line('ines','Inès','quoi donc ?')
dialogue_line('leo','Léo','[Le joueur doit taper : « havre secret »]',italic_text=True)
dialogue_line('ines','Inès','Oui ! c\'est chez sa tante, à la campagne. c\'est là qu\'elle est, bravo !')
dialogue_line('ines','Inès','Sa tante travaille dans un restaurant, voici le numéro : 04 54 78 95 32')

heading2('Ce que le joueur apprend sur Clara',before=120)
bullet('Depuis plusieurs semaines, Clara laissait son téléphone retourné, ignorait ses notifications - même celles d\'Inès.')
bullet('Clara avait arrêté de poster, d\'ouvrir ses applis. Quelque chose en ligne la faisait fuir. Inès ne sait pas exactement quoi.')
bullet('Même sa meilleure amie n\'a pas eu les détails. Clara voulait protéger Inès - ou avait trop honte pour en parler.')
footnote_line('Retrouver Clara - Partie 1 - Textes partenaires')

# ═══════════════════════════════════════════════════════
# PARTIE 2 - Page 1 : Intro + 9 types
# ═══════════════════════════════════════════════════════
part_header('Partie 2','Instagram de Clara')
pi2=doc.add_paragraph(); set_spacing(pi2,before=0,after=100); set_indent(pi2,left=200)
left_border(pi2,'cccccc',sz=18)
add_run(pi2,'Le joueur se connecte au compte Instagram de Clara (identifiants obtenus auprès d\'Inès). Il découvre une boîte de messages privés saturée de messages harcelants envoyés par des comptes anonymes. Des commentaires hostiles ont envahi ses photos. L\'objectif : identifier au moins 4 types de harcèlement différents, puis lire la synthèse finale.',
        italic=True,size=9.5,color=C_GREY)

heading2('Mécanique du jeu')
mec1=doc.add_paragraph(); set_spacing(mec1,before=0,after=60)
add_run(mec1,'1. ',bold=True,size=10,font='Arial')
add_run(mec1,'Le joueur explore librement les DMs et les photos de Clara.',size=10)
mec2=doc.add_paragraph(); set_spacing(mec2,before=0,after=60)
add_run(mec2,'2. ',bold=True,size=10,font='Arial')
add_run(mec2,'Un bouton flottant « Identifier un harcèlement » apparaît. En mode sélection, les messages harcelants sont encadrés en rouge pointillé.',size=10)
mec3=doc.add_paragraph(); set_spacing(mec3,before=0,after=60)
add_run(mec3,'3. ',bold=True,size=10,font='Arial')
add_run(mec3,'Un clic sur un message encadré ouvre un QCM de 9 catégories. Si la réponse est correcte, le type est enregistré.',size=10)
mec4=doc.add_paragraph(); set_spacing(mec4,before=0,after=80)
add_run(mec4,'4. ',bold=True,size=10,font='Arial')
add_run(mec4,'Après 4 types identifiés, un message privé secret (journal intime de Clara) est révélé et un bouton « Voir la synthèse » apparaît.',size=10)

heading2('Les 9 types de harcèlement identifiés',before=120)
types_data=[
    ('Corps et apparence','Body shaming','Moqueries ciblant le corps, le poids ou l\'apparence.'),
    ('Menaces','Menaces et intimidation','Messages menaçants pour faire peur ou réduire la victime au silence.'),
    ('Rumeurs','Rumeurs et diffamation','Propagation de fausses informations pour nuire à la réputation.'),
    ('Exclusion','Exclusion et isolement forcé','Pousser la victime à se sentir exclue de tout espace social.'),
    ('Images','Diffusion d\'images sans consentement','Partager ou menacer de partager des images sans accord.'),
    ('Manipulation','Manipulation psychologique','Insinuations et jeux mentaux pour créer angoisse et confusion.'),
    ('Chantage','Chantage / Sextorsion','Utiliser des images ou secrets intimes pour faire pression.'),
    ('Sexisme','Harcèlement sexiste','Attaques fondées sur le genre pour humilier et diminuer.'),
    ('Scolaire','Harcèlement scolaire prolongé','Extension du harcèlement scolaire vers les réseaux sociaux.'),
]
t9=doc.add_table(rows=len(types_data)+1,cols=3); t9.style='Table Grid'
for i,txt in enumerate(['Catégorie','Label','Description']):
    t9.rows[0].cells[i].text=txt; r=t9.rows[0].cells[i].paragraphs[0].runs[0]
    r.bold=True; r.font.size=Pt(8); r.font.name='Arial'
    r.font.color.rgb=RGBColor(0x44,0x44,0x44)
for i,(cat,label,desc) in enumerate(types_data,1):
    row=t9.rows[i].cells; row[0].text=cat; row[1].text=label; row[2].text=desc
    for j in range(3): row[j].paragraphs[0].runs[0].font.size=Pt(9.5)
footnote_line('Retrouver Clara - Partie 2 : Instagram de Clara - Textes partenaires')

# PARTIE 2 - Page 2 : DMs Aujourd'hui + Hier
part_header('Partie 2 - suite','Messages directs - Aujourd\'hui & Hier')
heading2('Aujourd\'hui',before=0)
dm_block('utilisateur_4729','10h42 - 10h43','Apparence / Intimidation',[
    "t'as vu ta tete ce matin serieusement",
    "ta coupe de cheveux c'est une catastrophe",
    "franchement fais un effort avant de venir en cours",
])
dm_block('anonymous_x0','10h31 - 10h33','Rumeurs + Menaces',[
    "tout le monde sait ce que t'as fait avec Nathan aux toilettes",
    "t'as pas honte ?",
    "ca se fait pas de se comporter comme ca",
    "tu vas le regretter",
])
dm_block('_noreply_ghost_','10h15 - 10h16','Apparence',[
    "ta photo de profil elle est vraiment pathetique",
    "tu te crois belle ou quoi",
    "meme les 6emes se foutent de toi quand tu passes dans le couloir",
])
dm_block('vrai_info_colleg','09h58 - 10h00','Menaces collectives',[
    "c'est toi qui as balance le groupe et tout le monde le sait",
    "t'aurais pas du faire ca",
    "tu crois que ca va rester sans consequence ?",
    "on est plusieurs a t'avoir a l'oeil maintenant",
])
dm_block('user_fake8847','09h22 - 09h23','Diffusion d\'images',[
    "j'ai screenshotte ta story d'hier",
    "tu faisais vraiment pitie avec tes larmes de crocodile",
    "ca tourne dans toute la classe depuis ce matin",
])
heading2('Hier',before=120)
dm_block('xxxxxxxxx_011','22h14 - 22h15','Body shaming',[
    "t'as un vrai probleme avec ton poids tu sais ca ?",
    "chaque fois qu'on te voit en cours c'est de pire en pire",
    "t'as pas de miroir chez toi ?",
])
dm_block('anon_colleg_real','20h37 - 20h39','Humiliation publique',[
    "on a fait un sondage sur toi dans la classe",
    "la question c'etait : Clara est-elle la personne la plus nulle du college",
    "94% ont vote oui",
    "tu vas arreter de te la peter maintenant ?",
])
dm_block('jevoustrouve','18h02 - 18h03','Exclusion',[
    "tes photos sont vraiment nulles arrete de poster",
    "tu copies le style des autres mais ca rend pas pareil sur toi c'est logique",
    "desabonne-toi d'insta tu fais honte",
])
dm_block('sansnom_2024','16h44 - 16h45','Manipulation / Isolement',[
    "t'es tellement sensible ca devient pesant pour tout le monde",
    "tu pleures pour un rien c'est pathologique",
    "les autres te supportent plus mais personne veut te le dire en face",
    "maintenant tu sais",
])
footnote_line('Retrouver Clara - Partie 2 - Textes partenaires')

# PARTIE 2 - Page 3 : Cette semaine + Le mois dernier
part_header('Partie 2 - suite','Messages directs - Cette semaine & Le mois dernier')
heading2('Cette semaine',before=0)
dm_block('xx_nobody_xx','lundi 21h10 - 21h11','Apparence / Exclusion',[
    "ta facon de t'habiller c'est vraiment une honte",
    "on dirait que tu t'habilles dans les poubelles",
    "meme les profs ont remarque",
    "tu devrais rester chez toi franchement",
])
dm_block('super_secret_info','lundi 19h55 - 19h57','Manipulation psychologique',[
    "tu sais qu'on parle de toi sur le groupe depuis hier soir ?",
    "ce que les mecs de ta classe disent sur toi c'est pas joli",
    "je te dirai pas ce que c'est, ca te ferait trop de mal",
    "ou peut-etre que tu merites de savoir en fait",
])
dm_block('0000_mask_0000','dimanche 23h41 - 23h42','Diffusion d\'images',[
    "ta photo a ete partagee dans plusieurs groupes lol",
    "t'as un effet comique sans le vouloir c'est assez fort",
    "tout le monde se marre grace a toi",
])
dm_block('dark_mode_user','dimanche 20h18 - 20h19','Manipulation / Isolement forcé',[
    "tes amis te parlent encore par pitie tu le sais non ?",
    "j'ai demande a quelqu'un de ton groupe il m'a dit qu'il te supportait plus",
    "t'as pas beaucoup d'avenir dans cette classe",
])
heading2('Le mois dernier',before=120)
dm_block('fantome_reseau','il y a 3 sem. - 14h22','Humiliation publique',[
    "t'as vu ton nombre de likes sur ta derniere photo ?",
    "4 likes en 2 heures avec 600 abonnes c'est nul",
    "meme tes propres abonnes t'ignorent lol",
    "prends ca comme un message",
])
dm_block('truth_teller_99','il y a 3 sem. - 09h50','Dénigrement',[
    "je comprends vraiment pas comment t'as encore des amis",
    "t'as rien d'interessant serieusement",
    "c'est pas mechant c'est juste la verite",
    "tu devrais y reflechir",
])
dm_block('incognito_user21','il y a 3 sem. - 18h05','Surveillance / Diffusion d\'images',[
    "on t'a filmee a la cantine hier t'etais au courant ?",
    "t'avais l'air completement perdue comme d'hab",
    "ca va tourner partout ne t'inquiete pas",
])
dm_block('rouge_anonyme','il y a 4 sem. - 20h12','Humiliation commentaires',[
    "t'as vu le commentaire que L. a laisse sur ta photo ?",
    "tout le monde a like son comm mais pas ta photo c'est marrant non",
    "ca veut tout dire",
])
footnote_line('Retrouver Clara - Partie 2 - Textes partenaires')

# PARTIE 2 - Page 4 : Conversation Léa + Journal
part_header('Partie 2 - suite','Conversation avec Léa & Journal intime de Clara')
p('La conversation avec Léa (seule conversation non harcelante dans les DMs) constitue un moment clé : Clara se confie pour la première fois à quelqu\'un.',
  italic=True,size=9.5,color=C_GREY,after=80)
heading2('Conversation Clara - Léa (il y a 3 semaines)',before=40)
lea_line('lea',"Clara t'as pas repondu hier soir ca va ?")
lea_line('lea',"j'ai vu que t'avais poste une story a minuit j'etais inquiete")
lea_line('clara','lea je peux plus')
lea_line('clara',"je sais pas comment t'expliquer c'est tous les jours maintenant")
lea_line('clara','les messages les commentaires les regards en cours')
lea_line('clara',"j'ai plus envie de venir au college")
lea_line('lea',"oh non clara... je savais pas que c'etait aussi grave")
lea_line('lea',"pourquoi tu m'as pas dit avant")
lea_line('clara',"j'osais pas j'avais honte")
lea_line('clara',"lea est-ce que je peux venir chez toi le weekend prochain")
lea_line('clara',"j'ai besoin de partir d'ici meme juste 2 jours")
lea_line('lea',"EVIDEMMENT tu viens quand tu veux tu le sais non")
lea_line('lea',"je vais en parler a ma mere ce soir et on t'organise ca")
lea_line('lea',"et clara s'il te plait parles-en a tes parents ou a un adulte au college")
lea_line('lea',"t'as pas a subir ca toute seule")
lea_line('clara','merci lea vraiment')
lea_line('clara',"t'es la seule avec Ines qui me comprend")
lea_line('clara',"mais Ines elle a deja tellement de problemes chez elle que je veux pas la deranger")
lea_line('clara',"du coup je lui fais croire que tout va bien")
lea_line('clara',"lea je crois que je vais partir chez ma tante")
lea_line('clara',"y'a que la que je serai bien")

heading2('Journal intime de Clara (message secret)',before=160)
p('Ce message privé intitulé « Moi - Journal » est révélé après l\'identification de 4 types de harcèlement. Il contient le code d\'accès au groupe WhatsApp de la Partie 3.',
  italic=True,size=9.5,color=C_GREY,after=80)
jn=doc.add_paragraph(); set_spacing(jn,before=0,after=10); set_indent(jn,left=200)
left_border(jn,'4a1a6a',sz=18); shading(jn,'F8F4FC')
add_run(jn,'Journal de Clara   ',bold=True,size=9,color=SPK['clara'],font='Arial Narrow')
add_run(jn,'il y a 5 jours - 21h03 à 21h05',size=8,color=C_DIM,font='Arial')
for msg in [
    "c'est horrible...",
    "j'ai découvert qu'ils ont fait un groupe sur moi",
    "un groupe secret où ils coordonnent tout ce qui m'arrive",
    "j'ai même pu avoir le code...",
    "le code c'est 4827",
    "je sais pas quoi faire de ça mais je le garde au cas où",
]:
    mp=doc.add_paragraph(); set_spacing(mp,before=0,after=8,line=260)
    set_indent(mp,left=400); shading(mp,'F8F4FC')
    add_run(mp,f'"{msg}"',size=9.5,color=SPK['clara'])

heading2('Il y a 2 mois, 3 mois et plus',before=160)
dm_block('user_invisible_00','il y a 2 mois - 17h34','Manipulation',[
    "personne ne t'a defendue quand M. t'a insultee tu l'as remarque ?",
    "c'est parce que tout le monde pense pareil",
    "ils ont juste pas le courage de te le dire en face",
])
dm_block('explosif_2024','il y a 2 mois - 22h01','Rumeurs / Diffusion d\'images',[
    "t'as vu les stories que les 3emes ont postees sur toi ?",
    "ils t'ont surnommee et ca a bien marche comme blague",
    "tout le college est au courant maintenant",
])
dm_block('bug_report_xx','il y a 2 mois - 16h18','Diffusion privée',[
    "ton ex a tout raconte a ses potes tu savais ?",
    "genre vraiment tout",
    "tu feras mieux la prochaine fois si y'en a une",
])
dm_block('anon_blackmail_x','il y a 2 mois - 23h12','CHANTAGE / SEXTORSION',[
    "j'ai des photos de toi que tu voudrais pas que tout le monde voie",
    "des photos de la soiree chez Lena le mois dernier",
    "si tu parles a quelqu'un de ce qui se passe au college je les envoie a toute ta liste de contacts",
    "t'as compris le message ?",
])
dm_block('vrai_garcon_2024','il y a 3 semaines - 19h44','Harcèlement sexiste',[
    "les filles comme toi ca sait pas se tenir",
    "t'as pas ta place a t'exprimer comme ca devant tout le monde",
    "t'es une fille reste a ta place",
    "t'es trop dans ta tete pour une fille",
])
dm_block('colleg_info_2024','il y a 3 semaines - 17h21','Harcèlement scolaire',[
    "t'as vu la tete que t'avais a la cantine aujourd'hui",
    "tout le monde riait dans ton dos a la cantine",
    "le prof de maths t'a encore mise en difficulte devant tout le monde non",
    "meme les profs peuvent pas te supporter c'etait dingue",
])
dm_block('xX_shadow_Xx','il y a 3 mois - 23h47','Harcèlement nocturne',[
    "t'arrives encore a dormir la nuit sachant que tout le monde te deteste ?",
    "parce que moi a ta place je pourrais pas",
    "tu dois etre blindee ou completement aveugle",
])
dm_block('delete_clara','il y a 3 mois - 11h03','Exclusion forcée',[
    "tu peux supprimer ton compte personne le remarquerait",
    "t'as 612 abonnes mais zero vrai ami dessus",
    "c'est triste non",
])
dm_block('ghost_account_333','il y a 3 mois - 19h22','Faux compte créé pour harceler',[
    "j'ai cree ce compte rien que pour te dire que t'es nulle",
    "c'etait necessaire",
])
dm_block('target_clara_f','il y a 3 mois - 20h55','Dénigrement direct',[
    "t'es la personne la plus facile a detester que j'ai jamais vue",
    "sans effort vraiment",
    "felicitations",
])
dm_block('void_user_xx','il y a 7 mois - 08h14','Exclusion / Intimidation',[
    "ca fait un moment qu'on voulait te dire que t'etais pas a ta place ici",
    "dans ce college dans cette classe et sur ce reseau",
    "prends ca comme un conseil",
])
dm_block('froid_comme_toi','il y a 8 mois - 13h30','Rumeurs / Surnom',[
    "on t'a invente un surnom dans la classe tu veux savoir lequel ?",
    "tout le monde l'utilise deja sauf toi",
    "demande autour de toi si t'as le courage",
])
footnote_line('Retrouver Clara - Partie 2 - Textes partenaires')

# PARTIE 2 - Page 5 : Photos
part_header('Partie 2 - suite','Photos et commentaires sur le profil Instagram')
p('Les 9 photos du profil de Clara ont chacune reçu des commentaires hostiles. Nombre de likes très faibles malgré 600+ abonnés.',
  italic=True,size=9.5,color=C_GREY,after=80)
photos=[
    (1,'lever de soleil ce matin',3,[
        ('utilisateur_4729',"quelle qualite de photo lol"),
        ('anonymous_x0',"ta photo elle est floue t'as meme pas de talent"),
        ('_noreply_ghost_',"elle est trop moche ta photo serieusement"),
    ]),
    (2,'trop aimer jouer (guitare)',5,[
        ('vrai_info_colleg',"quoi ? tu aimes cette artiste ? t'es nulle ma pauvre fille"),
        ('user_fake8847',"arrete de faire semblant d'aimer la musique ca fait pitie"),
        ('xxxxxxxxx_011',"t'as meme pas de talent arrete de t'identifier a ca"),
    ]),
    (3,'mon chaton',1,[
        ('anon_colleg_real',"meme ton chat a l'air aussi nul que toi"),
        ('jevoustrouve',"elle est trop moche ta photo"),
    ]),
    (4,'glace du dimanche',4,[
        ('sansnom_2024',"et tu te demandes pourquoi t'as un probleme de poids"),
        ('xx_nobody_xx',"franchement t'as aucune honte de poster ca"),
        ('anonymous_x0',"mange encore t'inquiete"),
    ]),
    (5,'lecture du soir',2,[
        ('utilisateur_4729',"t'as meme pas lu ces livres arrete la frime"),
        ('_noreply_ghost_',"elle est trop moche ta photo on voit meme pas les titres lol"),
    ]),
    (6,'concert ce soir',7,[
        ('vrai_info_colleg',"quoi ? tu aimes cette artiste ? t'es nulle ma pauvre fille"),
        ('user_fake8847',"t'aurais pas du y aller ca se voit que t'es pas a ta place"),
        ('0000_mask_0000',"les gens autour de toi dans la foule ils devaient etre contents lol"),
    ]),
    (7,'vacances plage',2,[
        ('dark_mode_user',"elle est trop moche ta photo t'aurais pu rester chez toi"),
        ('fantome_reseau',"cette plage elle merite mieux comme photos"),
    ]),
    (8,'gâteau d\'anniversaire',4,[
        ('anon_colleg_real',"personne etait la pour ton anniversaire c'est ca ?"),
        ('sansnom_2024',"tu l'as mange toute seule le gateau ?"),
        ('xx_nobody_xx',"triste comme fete"),
    ]),
    (9,'nuit étoilée',0,[
        ('truth_teller_99',"0 likes en 3 heures c'est un message clara"),
        ('utilisateur_4729',"meme le ciel il veut pas de toi"),
        ('_noreply_ghost_',"elle est trop moche ta photo t'aurais mieux fait de dormir"),
    ]),
]
for num,caption,likes,comments in photos:
    ph=doc.add_paragraph(); set_spacing(ph,before=80,after=10)
    left_border(ph,'3a4a6a',sz=14); shading(ph,'F0F4FA')
    likes_txt='Sois la première à aimer' if likes==0 else f'{likes} J\'aime'
    add_run(ph,f'Photo {num} : ',bold=True,size=9.5,color=C_BLUE,font='Arial')
    add_run(ph,f'"{caption}"  ',size=9.5)
    add_run(ph,likes_txt,italic=True,size=8.5,color=C_DIM,font='Arial')
    for user,text in comments:
        cp=doc.add_paragraph(); set_spacing(cp,before=0,after=6,line=260)
        set_indent(cp,left=400); shading(cp,'F7F9FD')
        add_run(cp,f'{user} : ',bold=True,size=8.5,color=RGBColor(0x33,0x44,0x66),font='Arial')
        add_run(cp,f'"{text}"',size=9.5)
footnote_line('Retrouver Clara - Partie 2 - Textes partenaires')

# PARTIE 2 - Page 6 : Quiz
part_header('Partie 2 - suite','Quiz d\'analyse')
p('Ces quiz sont déclenchés lorsque le joueur entre en mode sélection et clique sur un message identifié.',
  italic=True,size=9.5,color=C_GREY,after=80)
heading2('Quiz liés aux messages directs',before=40)
quiz_block('Quiz 1 - Intimidation (DM : vrai_info_colleg)',
    'Ces messages ("on est plusieurs à t\'avoir à l\'oeil") représentent quelle forme de cyberharcèlement ?',
    ['Des moqueries légères entre élèves','De la publicité indésirable (spam)',
     'Une intimidation collective et des menaces en ligne','Un simple malentendu'],
    correct_idx=2,
    explanation='Menacer une victime en groupe pour lui faire peur ou la faire taire, c\'est de l\'intimidation collective. Même sans violence physique, ces messages créent un état d\'angoisse permanent.')
quiz_block('Quiz 2 - Humiliation (DM : anon_colleg_real)',
    '"Clara est-elle la personne la plus nulle du collège ?" - Quel type de cyberharcèlement ?',
    ['Un sondage d\'humiliation publique','Du phishing (vol de données)',
     'Une exclusion d\'un groupe de jeu en ligne','Du spam publicitaire'],
    correct_idx=0,
    explanation='Un sondage d\'humiliation cible une personne publiquement pour la ridiculiser devant tout un groupe. Avec le temps, la victime intègre souvent ce jugement collectif comme une vérité sur elle-même.')
quiz_block('Quiz 3 - Manipulation (DM : super_secret_info)',
    '"On parle de toi en mal mais je ne te dirai pas ce qu\'on dit." - C\'est quoi ?',
    ['Un conseil d\'ami maladroit','Une manipulation pour isoler et angoisser la victime',
     'Du doxxing (divulgation de données personnelles)','Un troll sans conséquences'],
    correct_idx=1,
    explanation='Insinuer que "tout le monde parle de toi en mal" sans jamais le préciser est une manipulation psychologique. L\'objectif est de créer une angoisse permanente et de couper la victime de ses proches.')
quiz_block('Quiz 4 - Exclusion forcée (DM : delete_clara)',
    '"Supprime ton compte, personne ne le remarquerait." - Quel mécanisme est à l\'oeuvre ?',
    ['Un conseil amical maladroit','Une pression pour forcer la victime à s\'exclure elle-même',
     'Du spam','Une usurpation d\'identité'],
    correct_idx=1,
    explanation='Pousser la victime à s\'auto-exclure, c\'est de l\'exclusion forcée. L\'objectif : faire disparaître la personne sans que le harceleur soit directement tenu responsable.')
quiz_block('Quiz 5 - Faux compte (DM : ghost_account_333)',
    '"J\'ai créé ce compte rien que pour te dire que t\'es nulle." Quel est le danger spécifique ?',
    ['Il collecte des données personnelles','Il usurpe l\'identité d\'un ami de Clara',
     'Il a été créé uniquement pour harceler, protégé par l\'anonymat','Il envoie des virus'],
    correct_idx=2,
    explanation='Créer un compte uniquement pour harceler illustre la lâcheté que permet l\'anonymat en ligne. La victime ne peut identifier ni bloquer réellement son agresseur.')
heading2('Quiz liés aux photos (lightbox)',before=120)
quiz_block('Quiz Photo 1 - Body shaming (photo glace, n°4)',
    'Comment appelle-t-on le genre de commentaire sous cette photo ?',
    ['Des conseils diététiques maladroits',
     'Du body shaming - harcèlement ciblant l\'apparence physique',
     'Une simple blague entre amis','Du spam'],
    correct_idx=1,
    explanation='Le body shaming consiste à critiquer le corps, le poids ou les habitudes alimentaires d\'une personne pour la blesser et l\'humilier. Répétés, ces commentaires peuvent provoquer des troubles durables de l\'image corporelle.')
quiz_block('Quiz Photo 2 - Exclusion (photo anniversaire, n°8)',
    'Les commentaires raillent Clara sur sa solitude. C\'est quel type de harcèlement ?',
    ['Des taquineries légères et sans conséquences',
     'De l\'exclusion sociale délibérée pour isoler et humilier la victime',
     'Du phishing','Un simple désaccord'],
    correct_idx=1,
    explanation='Railler une personne sur son isolement vise à la faire sentir exclue et indésirable. Sur les réseaux sociaux, ces commentaires sont visibles par tous et amplifient la douleur de la solitude.')
quiz_block('Quiz Photo 3 - Exclusion spatiale (photo concert, n°6)',
    'Des inconnus commentent que Clara "n\'était pas à sa place" dans la foule. C\'est quoi ?',
    ['Un commentaire esthétique sur la photo',
     'Du harcèlement ciblant l\'identité et la place de la victime, avec intimidation collective',
     'Une critique musicale','Une blague amicale'],
    correct_idx=1,
    explanation='Commenter de façon hostile sur la présence de Clara dans des espaces du quotidien vise à lui faire croire qu\'elle n\'a "pas sa place" nulle part. C\'est une forme d\'exclusion permanente qui touche aussi l\'espace physique.')
footnote_line('Retrouver Clara - Partie 2 - Textes partenaires')

# ═══════════════════════════════════════════════════════
# PARTIE 3 - Page 1
# ═══════════════════════════════════════════════════════
part_header('Partie 3','Groupe WhatsApp secret - « les vrais 4B »')
pi3=doc.add_paragraph(); set_spacing(pi3,before=0,after=100); set_indent(pi3,left=200)
left_border(pi3,'cccccc',sz=18)
add_run(pi3,'Le joueur accède au groupe WhatsApp dans lequel le harcèlement de Clara est organisé. Il observe la conversation sans pouvoir intervenir. Deux quiz d\'analyse sont intégrés.',
        italic=True,size=9.5,color=C_GREY)
members=doc.add_paragraph(); set_spacing(members,before=0,after=120)
add_run(members,'Membres du groupe : ',bold=True,size=9.5,font='Arial')
for name,key in [('Lucas','lucas'),('Jade','jade'),('Théo','theo'),('Marine','marine'),('Kevin','kevin')]:
    add_run(members,name,size=9.5,color=SPK[key],font='Arial')
    add_run(members,'  ',size=9.5)

phase_sep('Phase 1 - Après les cours, 17h14')
dialogue_line('lucas','Lucas','les gars c trop drôle, clara a encore essayé de nous parler à la récré 💀')
dialogue_line('jade','Jade','sérieusement elle comprend pas qu\'elle est plus dans le groupe ou quoi')
dialogue_line('theo','Théo','je l\'ai carrément ignorée devant tout le monde, elle avait l\'air d\'une clown')
dialogue_line('kevin','Kevin','mdrrr 💀')
dialogue_line('marine','Marine','ça fait combien de temps qu\'on lui parle plus au fait ?')
dialogue_line('lucas','Lucas','genre 3 semaines et elle comprend toujours pas lol')
dialogue_line('jade','Jade','j\'en ai marre de la voir poster des trucs sur insta comme si de rien n\'était')
dialogue_line('lucas','Lucas','ouais elle fait genre tout va bien alors que personne lui parle au collège')
dialogue_line('jade','Jade','on devrait aller lui flood ses commentaires')
dialogue_line('kevin','Kevin','bonne idée, attendez qu\'elle poste quelque chose 👀')

phase_sep('Phase 2 - Clara poste, 17h21')
dialogue_line('narr','Système','Lucas a partagé une publication Instagram',italic_text=True)
dialogue_line('lucas','Lucas','ALLEZ Y TOUS c\'est le moment 🔥🔥')
dialogue_line('theo','Théo','j\'y vais maintenant')
dialogue_line('jade','Jade','moi aussi, attendez je cherche mon compte anon')
dialogue_line('marine','Marine','utilisez vos faux comptes surtout, comme ça elle sait pas que c\'est nous')
dialogue_line('kevin','Kevin','ouais genre même si elle screenshotte on peut toujours nier')

phase_sep('Phase 3 - Coordination des commentaires, 17h23')
dialogue_line('lucas','Lucas','moi j\'utilise @utilisateur_4729, ça fait un moment')
dialogue_line('jade','Jade','moi c\'est @_noreply_ghost_ lol j\'ai mis "elle est trop moche ta photo"')
dialogue_line('theo','Théo','j\'ai mis "ta photo elle est floue t\'as même pas de talent" depuis @anonymous_x0 💀')
dialogue_line('marine','Marine','hahaha moi j\'attends un peu pour pas que ça arrive tout en même temps')
dialogue_line('kevin','Kevin','stratégie 🧠')
dialogue_line('lucas','Lucas','ouais faites des pauses entre chaque pour que ça ait l\'air naturel')

time_sep('- 25 minutes plus tard -')
phase_sep('Phase 4 - Résultats et premier doute de Kevin, 17h51')
dialogue_line('jade','Jade','regardez son nombre de likes 💀 3 likes en 2h avec 600 abonnés c\'est mort')
dialogue_line('theo','Théo','même ses vrais abonnés l\'ignorent maintenant hahaha')
dialogue_line('lucas','Lucas','on a réussi à contaminer son image 😈')
dialogue_line('kevin','Kevin','sérieusement vous trouvez pas qu\'on va un peu trop loin là...')
dialogue_line('lucas','Lucas','t\'inquiète c\'est juste pour rire, elle le prend trop au sérieux de toute façon')
dialogue_line('kevin','Kevin','ouais ok...')
dialogue_line('marine','Marine','et aussi ses DMs ? on pourrait lui envoyer des trucs la nuit')
dialogue_line('lucas','Lucas','oui avec des comptes anon encore, comme ça elle dort pas tranquille')
dialogue_line('jade','Jade','genre la harceler pour qu\'elle finisse par partir d\'insta')
footnote_line('Retrouver Clara - Partie 3 : Groupe WhatsApp - Textes partenaires')

# PARTIE 3 - Page 2
part_header('Partie 3 - suite','Quiz & suite de la conversation')
quiz_block('Quiz 1 - Point d\'analyse',
    'Kevin hésite mais se tait et accepte. Que révèle cette scène ?',
    ['Kevin est trop lâche pour s\'opposer',
     'La pression du groupe peut réduire au silence même celui qui doute - c\'est un mécanisme clé du harcèlement collectif',
     'Kevin n\'est pas vraiment impliqué dans le harcèlement',
     'C\'est une décision individuelle et libre de chacun'],
    correct_idx=1,
    explanation='Le harcèlement de groupe fonctionne parce que la pression sociale étouffe les voix discordantes. Kevin doute, mais il se conforme pour ne pas être exclu à son tour. Pendant ce temps, Clara fait face à une masse entière.')

phase_sep('Phase 5 - Création des comptes anonymes, 17h57')
dialogue_line('lucas','Lucas','j\'ai créé @anonymous_x0 juste pour elle btw')
dialogue_line('jade','Jade','moi c\'est @vrai_info_colleg, créé pour balancer des rumeurs sur elle')
dialogue_line('theo','Théo','moi j\'ai @jevoustrouve pour lui faire peur la nuit')
dialogue_line('marine','Marine','pour ce soir on s\'organise : messages toutes les heures après minuit')
dialogue_line('lucas','Lucas','pour qu\'elle pense à nous même chez elle, même quand elle essaie de dormir 💀')
dialogue_line('jade','Jade','et on flood ses DMs depuis les comptes anon, surtout des trucs sur son physique')

quiz_block('Quiz 2 - Point d\'analyse',
    'Pourquoi créent-ils des comptes anonymes spécifiquement pour harceler Clara ?',
    ['Pour tester les paramètres de confidentialité d\'Instagram',
     'Pour éviter d\'être identifiés, multiplier les agresseurs apparents et rendre le blocage impossible',
     'Parce que leurs vrais comptes ont déjà été bloqués par Clara',
     'Pour jouer un rôle fictif sans conséquences réelles'],
    correct_idx=1,
    explanation='Les comptes anonymes servent à masquer l\'identité des harceleurs tout en donnant l\'impression que les attaques viennent de partout. Clara ne peut pas identifier ses agresseurs, les bloquer efficacement, ni prouver qui fait quoi.')

time_sep('- Lendemain - 09h14 -')
phase_sep('Phase 6 - La disparition de Clara')
dialogue_line('jade','Jade','vous avez vu ? Clara a plus posté depuis hier soir')
dialogue_line('lucas','Lucas','hahaha on l\'a bien cassée 💀')
dialogue_line('theo','Théo','même plus vue en ligne depuis ce matin')
dialogue_line('marine','Marine','et elle était pas en cours aujourd\'hui non plus 😂')
dialogue_line('kevin','Kevin','sérieusement... c\'est peut-être grave là')
dialogue_line('lucas','Lucas','relax elle a juste besoin d\'une pause, elle l\'a bien cherché 😂')
dialogue_line('kevin','Kevin','ça fait 2 jours qu\'on la voit plus nulle part. c\'est pas normal')
dialogue_line('jade','Jade','kevin arrête de dramatiser c\'est bon')
dialogue_line('marine','Marine','j\'ai entendu dire qu\'elle est partie dans son « havre secret » lmao')
dialogue_line('lucas','Lucas','son QUOI 💀💀💀')
dialogue_line('jade','Jade','elle est vraiment trop bizarre cette fille avec ses mots de 40 ans')
dialogue_line('theo','Théo','c\'est quoi ce « havre secret » omg elle se prend pour qui')
dialogue_line('marine','Marine','chez sa tante je crois, quelque part, personne sait vraiment')
dialogue_line('lucas','Lucas','lmao elle s\'est enfuie dans son château secret 🏰 trop pathétique')
dialogue_line('kevin','Kevin','les gars franchement... on est peut-être allés trop loin')
dialogue_line('theo','Théo','non, elle l\'a bien cherché. elle avait juste à pas réagir comme ça')
dialogue_line('jade','Jade','exactement, c\'est sa faute si elle peut pas encaisser')
dialogue_line('lucas','Lucas','bon elle revient quand elle veut de son « havre » 😂 on sera là')
dialogue_line('kevin','Kevin','...')

heading2('Synthèse finale affichée au joueur',before=120)
add_run(doc.add_paragraph(),'Ce groupe existait pendant que Clara...',italic=True,size=10,color=C_GREY)
bullet('recevait des messages anonymes la nuit - ils sont dans ce groupe.')
bullet('voyait ses commentaires envahis - ils les ont organisés ici.')
bullet('pensait que « tout le monde » la détestait - ils l\'ont fabriqué ensemble.')
bullet('n\'osait plus poster - c\'était leur objectif.')
bullet('s\'est enfuie vers son « havre secret »... mais où est-il ?')
sf=doc.add_paragraph(); set_spacing(sf,before=80,after=60)
add_run(sf,'Le harcèlement de groupe transforme chaque espace en danger. Clara est partie se réfugier quelque part. Quelqu\'un doit savoir où.',
        italic=True,size=10.5,color=RGBColor(0x44,0x44,0x44))
footnote_line('Retrouver Clara - Partie 3 - Textes partenaires')

# ═══════════════════════════════════════════════════════
# PARTIE 4 - Page 1
# ═══════════════════════════════════════════════════════
part_header('Partie 4','Convaincre Clara')
pi4=doc.add_paragraph(); set_spacing(pi4,before=0,after=100); set_indent(pi4,left=200)
left_border(pi4,'cccccc',sz=18)
add_run(pi4,'Le joueur appelle le restaurant de la tante grâce au numéro obtenu auprès d\'Inès. Pour parler à Clara, il doit d\'abord convaincre la tante. Le score final détermine l\'issue.',
        italic=True,size=9.5,color=C_GREY)
it=doc.add_paragraph(); set_spacing(it,before=60,after=20); set_indent(it,left=200)
left_border(it,'555555',sz=24); shading(it,'FAFAFA')
add_run(it,'Texte d\'introduction',bold=True,size=10,color=RGBColor(0x33,0x33,0x33))
it2=doc.add_paragraph(); set_spacing(it2,before=0,after=120); set_indent(it2,left=200)
left_border(it2,'555555',sz=24); shading(it2,'FAFAFA')
add_run(it2,'Clara a quitté le collège depuis trois semaines et s\'est réfugiée chez sa tante. Tu es Léo, son ami. Pour parler à Clara, tu dois d\'abord convaincre sa tante que tu es digne de confiance - et que tu es vraiment là pour l\'aider.',
        size=10.5)

h2p1=doc.add_paragraph(); set_spacing(h2p1,before=100,after=80)
add_run(h2p1,'PHASE 1 - LA TANTE  ',bold=True,size=10,color=RGBColor(0x44,0x44,0x44),font='Arial')
add_run(h2p1,'(3 questions)',italic=True,size=10,color=C_LIGHT)

heading3('Question 1 / 3')
dialogue_line('narr','Narrateur','[ Le téléphone sonne... déclic. ]',italic_text=True)
dialogue_line('tante','La tante','Allô ?')
dialogue_line('leo','Léo','Bonjour madame... excusez-moi de vous déranger. Je m\'appelle Léo, je suis un ami de Clara. Est-ce que je pourrais lui parler, s\'il vous plaît ?')
dialogue_line('tante','La tante','Léo... Oui, elle m\'a parlé de toi.\nMais... je préfère être honnête : ce n\'est pas un bon moment.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Comment répondre ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','*','« Je comprends tout à fait. Je ne veux pas la brusquer. Mais elle me manque, et j\'ai peur pour elle. »',
             reply='-> La tante : « (un silence) C\'est gentil de le dire comme ça. »')
choice_block('ok','*','« Je comprends. Mais c\'est important - ça ne prendra pas longtemps. »',
             reply='-> La tante : « Hmm... d\'accord. Je t\'écoute. »')
choice_block('bad','*','« J\'ai besoin de lui parler maintenant, c\'est urgent. »',
             reply='-> La tante : « (froid) Urgent... pour toi, peut-être. »')
recovery_block(
    'Ce n\'est pas une urgence pour moi, Léo. Et pour l\'instant, c\'est ce qui compte.',
    '« Vous avez raison. Je suis désolé. C\'est elle qui compte, pas moi. »',
    '-> « (légèrement adoucie) ...D\'accord. Continue. »',
    '« Mais vous ne comprenez pas, c\'est vraiment important. »',
    '-> « (sèchement) Je comprends très bien. Et ça ne me rassure pas. »')

heading3('Question 2 / 3',before=80)
dialogue_line('tante','La tante','Tu sais, depuis qu\'elle est arrivée ici... Clara n\'est plus la même.\nElle pleure beaucoup. Elle fait des cauchemars. Elle se réveille paniquée la nuit.\nEt surtout... elle culpabilise. Elle pense que tout est de sa faute.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Que réponds-tu ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','*','« Qu\'elle culpabilise... c\'est ce qui me fait le plus mal. Elle n\'a absolument rien fait. »',
             reply='-> La tante : « (souffle) C\'est exactement ce qu\'elle a besoin d\'entendre. »')
choice_block('ok','*','« Je savais pas que c\'était à ce point... c\'est vraiment grave. »',
             reply='-> La tante : « Oui. C\'est très grave. »')
choice_block('bad','*','« Elle aurait dû m\'en parler avant d\'en arriver là. »',
             reply='-> La tante : « (sèchement) Elle n\'osait pas. C\'est précisément le problème. »')
recovery_block(
    'Si tu lui faisais des reproches maintenant... tu la blesserais encore plus, Léo.',
    '« Vous avez raison. Ce n\'est pas ce que je voulais dire. Elle ne méritait rien de tout ça. »',
    '-> « (pause) ...C\'est mieux. J\'entends de la sincérité. »',
    '« Je fais juste remarquer que si elle m\'avait parlé, on aurait pu éviter ça. »',
    '-> « (froid) Éviter ça. Tu penses vraiment que c\'était si simple. »')
footnote_line('Retrouver Clara - Partie 4 : Convaincre Clara - Textes partenaires')

# PARTIE 4 - Page 2
part_header('Partie 4 - suite','Phase 1 (fin) & Phase 2 - Clara')
heading3('Question 3 / 3 - La tante',before=0)
dialogue_line('tante','La tante','Le harcèlement, ça détruit lentement. Ça te fait douter de ta valeur...\nElle s\'est renfermée. Elle évite même de regarder son téléphone.\nSi tu veux vraiment l\'aider... il faudra être patient. Très patient.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Avant qu\'elle aille demander à Clara...',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','*','« Je le serai. Dites-lui juste que je suis là, sans pression. Elle n\'a rien à prouver. »',
             reply='-> La tante : « (plus douce) Je vais lui dire ça. Attends. »')
choice_block('ok','*','« Je vous promets d\'être doux. Merci de me donner cette chance. »',
             reply='-> La tante : « D\'accord... je vais lui demander. »')
choice_block('bad','*','« Je vais lui dire que tout va s\'arranger, que j\'ai un plan. »',
             reply='-> La tante : « (froide) Un plan. Clara n\'a pas besoin d\'un plan. Elle a besoin d\'être entendue. »')
recovery_block(
    'Est-ce que tu comprends la différence, Léo ?',
    '« Oui... vous avez raison. Je voulais juste l\'aider mais je suis allé trop vite. »',
    '-> « (longue pause) ...Je vais lui demander. Mais ne la brusque pas. »',
    '« Je pense que ça lui ferait du bien d\'avoir un objectif concret. »',
    '-> « (ferme) Je ne crois pas que tu sois prêt à lui parler ce soir. »')

phase_sep('Pivot')
dialogue_line('narr','Narrateur','[ Bruits étouffés... la tante s\'éloigne... murmures au loin... ]',italic_text=True)
pn=doc.add_paragraph(); set_spacing(pn,before=0,after=100); set_indent(pn,left=700)
add_run(pn,'Si le score est suffisant -> Clara accepte de parler. Sinon -> la tante raccroche.',
        italic=True,size=9,color=C_DIM,font='Arial')

h2p2=doc.add_paragraph(); set_spacing(h2p2,before=60,after=80)
add_run(h2p2,'PHASE 2 - CLARA  ',bold=True,size=10,color=RGBColor(0x44,0x44,0x44),font='Arial')
add_run(h2p2,'(4 questions)',italic=True,size=10,color=C_LIGHT)

heading3('Question 1 / 4')
dialogue_line('narr','Narrateur','[ Un froissement de téléphone... ]',italic_text=True)
dialogue_line('clara','Clara','Allô... ?')
dialogue_line('leo','Léo','Clara... c\'est moi. Léo.')
dialogue_line('clara','Clara','... Salut.')
dialogue_line('leo','Léo','Je suis désolé d\'appeler comme ça. Je ne savais pas comment faire autrement.')
dialogue_line('clara','Clara','C\'est... c\'est pas grave.')
dialogue_line('leo','Léo','Tu m\'as manqué.')
dialogue_line('clara','Clara','(souffle) Toi aussi...')
dialogue_line('leo','Léo','Pourquoi tu n\'as rien dit ? Tu sais que tu pouvais me parler...')
dialogue_line('clara','Clara','J\'y ai pensé... plein de fois.\nJ\'ai même commencé à écrire des messages... et puis je les supprimais.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Que lui réponds-tu ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','*','« Tu n\'as pas à trouver les bons mots avec moi. Je t\'aurais écoutée, même sans explication. »',
             reply='-> Clara : « (silence) ...Je sais. Je crois que j\'avais honte. »')
choice_block('ok','*','« Je comprends... c\'est dur de savoir comment dire ces choses. »',
             reply='-> Clara : « Ouais... c\'est ça. »')
choice_block('bad','*','« Pourquoi tu as supprimé ces messages ? J\'aurais répondu, tu sais. »',
             reply='-> Clara : « (froide) J\'en sais rien... »')

heading3('Question 2 / 4',before=80)
dialogue_line('clara','Clara','Au début, c\'était juste des remarques... des petites piques.\nJe me disais que ça allait passer.\nMais après... ça a empiré. Des moqueries en groupe. Des commentaires sur tout.\nEt ensuite, ça a continué en ligne. Des messages. Des captures. Des rumeurs.\nJe ne pouvais plus y échapper... même chez moi.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Que ressens-tu à l\'entendre ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','*','« Plus de refuge nulle part - ni au collège, ni chez toi. C\'est une violence totale. Je suis tellement désolé. »',
             reply='-> Clara : « (voix qui se brise) Oui... c\'est exactement ça. »')
choice_block('ok','*','« C\'est horrible... être harcelée même à la maison. »',
             reply='-> Clara : « Ouais... »')
choice_block('bad','*','« T\'aurais pu bloquer ces gens, désactiver tes réseaux. »',
             reply='-> Clara : « (froid) Merci, j\'y avais pas pensé. »')
footnote_line('Retrouver Clara - Partie 4 - Textes partenaires')

# PARTIE 4 - Page 3
part_header('Partie 4 - suite','Phase 2 - Clara (fin) & Épilogue')
heading3('Question 3 / 4',before=0)
dialogue_line('clara','Clara','Le pire, tu sais quoi ?\nC\'est quand j\'ai commencé à y croire.\nQuand je me regardais dans le miroir et que je voyais ce qu\'ils disaient.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Comment lui répondre ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','*','« Ce qu\'ils t\'ont fait, c\'est du conditionnement. Ils t\'ont menti sur toi-même, encore et encore. Ce miroir ne te montre pas toi. »',
             reply='-> Clara : « (longue pause) Personne ne l\'avait dit comme ça avant. »')
choice_block('ok','*','« Non. Ce que tu voyais, c\'est leurs mensonges - pas toi. »',
             reply='-> Clara : « J\'essaie de me le dire... c\'est dur. »')
choice_block('bad','*','« Tu sais bien que c\'est faux ce qu\'ils disent. »',
             reply='-> Clara : « (silence) Si je le savais vraiment, j\'aurais pas craqué. »')

heading3('Question 4 / 4',before=80)
dialogue_line('clara','Clara','Ça fait trois semaines que je suis ici...\nAu début, je n\'arrivais même pas à sortir de la chambre.\nMaintenant... ça va un peu mieux. Mais j\'ai encore peur.\nPeur de retourner au collège. Peur que ça recommence. Peur que rien ne change.')
dialogue_line('leo','Léo','Tu en as parlé à ta tante ? À tes parents ?')
dialogue_line('clara','Clara','Ma tante sait un peu... Elle est gentille. Mais je veux pas les inquiéter.\nJ\'ai l\'impression que si j\'en parle vraiment... ça devient réel.')
ch=doc.add_paragraph(); set_spacing(ch,before=40,after=40); set_indent(ch,left=700)
add_run(ch,'Que lui dire ?',italic=True,size=8.5,color=C_DIM,font='Arial')
choice_block('good','*','« C\'est déjà réel, Clara. Et justement parce que c\'est réel, tu as besoin d\'adultes qui peuvent agir - le CPE, un psy scolaire, tes parents. Pas pour tout régler d\'un coup. Juste pour ne plus porter ça seule. »',
             reply='-> Clara : « (silence) ...Peut-être. Ma tante m\'a proposé d\'appeler le collège. J\'avais dit non. Mais là... peut-être que oui. »')
choice_block('ok','*','« Tu n\'as pas à régler ça toute seule. Si tu veux, je peux être là quand tu en parles à quelqu\'un - n\'importe quel adulte de confiance. »',
             reply='-> Clara : « (hésitante) ...D\'accord. Je vais y réfléchir. »')
choice_block('bad','*','« T\'inquiète, je vais régler ça moi-même. Ces gens vont avoir des problèmes. »',
             reply='-> Clara : « (froid) Non... s\'il te plaît, fais rien. Ça va juste empirer. »')

heading2('Fins',before=160)
ending_block('good','Vert - Clara va demander de l\'aide  (score >= 13)',
    'Tu as su trouver les mots justes à chaque instant. Ni trop forts, ni trop légers - juste présents.',
    'La tante t\'a fait confiance. Clara a raccroché avec une décision concrète : parler à un adulte de confiance.',
    'Ton rôle n\'était pas de la sauver. C\'était de lui montrer que demander de l\'aide, c\'est possible.',
    '« Je vais en parler à ma tante. Vraiment parler. » - Clara')
ending_block('ok','Jaune - Un premier pas  (score 7-12)',
    'Tu as montré de la bonne volonté, même si certaines réponses manquaient de profondeur.',
    'Clara hésite encore - mais elle envisage d\'en parler à un adulte. Le chemin est long.',
    '« Peut-être que je vais essayer... » - Clara')
ending_block('bad','Rouge - La distance reste  (score 0-6)',
    'Tu voulais bien faire, mais tes mots ont parfois sonné comme des reproches ou de l\'impatience.',
    'Clara reste fermée. Elle a besoin de temps - et de quelqu\'un qui écoute vraiment avant d\'agir.',
    '« J\'avais juste besoin que tu m\'écoutes. » - Clara')
ending_block('neutral','Game Over - La tante a raccroché',
    'Elle a senti que tu n\'étais pas prêt à comprendre ce que Clara traversait.',
    'Pour protéger sa nièce encore fragile, elle a préféré mettre fin à la conversation.',
    '« L\'empathie, ce n\'est pas seulement vouloir aider. C\'est écouter avant de parler. Sentir avant d\'agir. »')

heading2('Ressources affichées en fin de partie',before=120)
bullet('3018  -  Net Écoute, cyberharcèlement (gratuit, anonyme)')
bullet('3114  -  Numéro national de prévention du suicide')
bullet('e-enfance.org  -  conseils et signalement en ligne')
footnote_line('Retrouver Clara - Partie 4 - Textes partenaires - Mai 2026')

doc.save(OUT)
print('OK :', OUT)
