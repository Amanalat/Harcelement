var TEXTES = {

  // ─── Interface ────────────────────────────────────────────────────────────

  contact: {
    name:          "Inès",
    avatar:        "IN",
    statusOnline:  "en ligne",
    statusTyping:  "écrit…"
  },

  // Index 0 = trust -4, index 4 = trust 0, index 8 = trust +4
  trustLabels: [
    "elle ne veut plus te parler",
    "elle est sur le point de raccrocher",
    "elle se méfie de toi",
    "elle hésite à répondre",
    "elle t'écoute",
    "elle commence à te faire confiance",
    "elle te fait confiance",
    "elle te fait confiance",
    "elle te fait vraiment confiance"
  ],
  trustInitial: "elle hésite à répondre",

  choiceHint:       "Que répond Léo ?",
  choiceHintCrise:  "Comment réagit Léo ?",
  restartBtn:       "↺ Recommencer",
  revelationsHeader:"📋 CE QUE TU AS APPRIS SUR CLARA",

  // ─── Séquence d'ouverture ─────────────────────────────────────────────────

  ouverture: [
    { t: "Inès ?",                                                                    type: 's' },
    { t: "Oui c'est qui",                                                             type: 'r' },
    { t: "C'est Léo. On est dans la même école que Clara.",                           type: 's' },
    { t: "Je te connais pas.",                                                        type: 'r' },
    { t: "Je sais. J'arrive plus à la joindre depuis hier soir. T'as eu de ses nouvelles ?", type: 's' },
    { t: "Pourquoi tu me demandes ça à moi",                                         type: 'r' }
  ],

  // ─── Messages de fin rapide / blocage ────────────────────────────────────

  finImmediate: [
    { t: "ok",    type: 'r'  },
    { t: "vu ✔️", type: 'sy' }
  ],

  blocageMessages: [
    { t: "Arrête de me parler.",  type: 'cr' },
    { t: "Je te répondrai plus.", type: 'cr' },
    { t: "(elle ne répond plus)", type: 'sy' }
  ],

  // ─── Révélations ─────────────────────────────────────────────────────────

  REVELATIONS: [
    {
      icon:  '📵',
      title: 'Elle fuyait son téléphone',
      txt:   "Depuis plusieurs semaines, Clara laissait son téléphone retourné, ignorait ses notifications — même celles d'Inès."
    },
    {
      icon:  '🔒',
      title: 'Elle avait disparu des réseaux',
      txt:   "Clara avait arrêté de poster, d'ouvrir ses applis. Quelque chose en ligne la faisait fuir. Inès ne sait pas exactement quoi."
    },
    {
      icon:  '❓',
      title: "Inès ne sait pas tout",
      txt:   "Même sa meilleure amie n'a pas eu les détails. Clara voulait protéger Inès — ou avait trop honte pour en parler."
    }
  ],

  // ─── Scénario principal ───────────────────────────────────────────────────

  G: [

    // Étape 0 — Pourquoi Léo contacte Inès
    {
      c: [
        { l: 'A', t: "Parce que t'es son amie. Si quelqu'un sait quelque chose, c'est toi.", e: -1 },
        { l: 'B', t: "Je savais pas à qui d'autre m'adresser.",                              e:  0 },
        { l: 'C', t: "Je suis inquiet. J'arrive plus à dormir depuis hier soir.",            e:  1 }
      ]
    },

    // Étape 1 — Inès vérifie qui est Léo
    {
      intro: [
        "Tu la connais comment toi, Clara ?"
      ],
      c: [
        { l: 'A', t: "On se croise souvent. Je l'aimais bien.",                               e:  1 },
        { l: 'B', t: "Pas super bien. Mais j'ai entendu parler d'elle ces derniers temps.",   e: -1 },
        { l: 'C', t: "On est dans des classes différentes mais on se parle des fois.",        e:  0 }
      ]
    },

    // Étape 2 — Clara ne répond plus à personne
    {
      intro: [
        "Elle répond plus à moi non plus.",
        "Depuis quelques jours."
      ],
      c: [
        { l: 'A', t: "Ça lui arrivait déjà avant ?",      e:  1 },
        { l: 'B', t: "Peut-être qu'elle vous a bloqués.", e: -1 },
        { l: 'C', t: "Vous vous parliez souvent ?",       e:  0 }
      ]
    },

    // Étape 3 — Ça faisait un moment qu'elle n'allait pas bien
    {
      intro: [
        "Non. Jamais.",
        "Ça faisait un moment qu'elle était pas bien.",
        "Depuis le mois dernier au moins.",
        "Elle manquait des cours. Elle répondait plus aux messages.",
        "Elle disait que c'était rien."
      ],
      c: [
        { l: 'A', t: "Tu sais ce qui s'est passé ?",              e:  1 },
        { l: 'B', t: "Et t'as pas essayé d'en parler avec elle ?", e: -1 },
        { l: 'C', t: "Elle avait l'air d'avoir peur de quelque chose ?", e: 0 }
      ]
    },

    // Étape 4 — La peur du téléphone (sans explication)
    {
      intro: [
        "Si j'ai essayé.",
        "Elle voulait pas.",
        "Mais je voyais bien.",
        "Elle laissait son téléphone retourné sur la table. Elle regardait plus ses applis.",
        "Des fois je lui envoyais un message, je voyais qu'elle l'avait lu… et elle répondait pas pendant des heures."
      ],
      c: [
        { l: 'A', t: "On dirait qu'elle voulait s'éloigner de son téléphone.", e:  1 },
        { l: 'B', t: "C'est bizarre comme comportement.",                      e:  0 },
        { l: 'C', t: "C'est peut-être juste une mauvaise période.",            e: -1 }
      ]
    },

    // Étape 5 — Inès hésite à en dire plus
    {
      intro: [
        "Je sais pas si je devrais te raconter tout ça.",
        "Je te connais même pas."
      ],
      c: [
        { l: 'A', t: "T'es obligée à rien. C'est toi qui décides.",                    e:  1 },
        { l: 'B', t: "Dis-moi juste ce que tu sais.",                                  e: -1 },
        { l: 'C', t: "Je veux juste savoir si elle va bien. Rien d'autre.",            e:  0 }
      ]
    }

  ],

  // ─── Crise de confiance ───────────────────────────────────────────────────

  CRISIS: {
    intro: [
      "Attends.",
      "T'es dans quelle classe ?",
      "Tu connais qui dans la sienne ?"
    ],
    c: [
      { l: 'A', t: "T'as raison d'être méfiante. Tu me connais pas.",                     e:  2 },
      { l: 'B', t: "Je fais pas partie des gens qui lui ont fait du mal.",                e:  1 },
      { l: 'C', t: "Fais-moi confiance, j'essaie juste d'aider.",                        e: -1 }
    ]
  },

  // ─── Fins ─────────────────────────────────────────────────────────────────

  fins: {

    imm: {
      titre: "Fin de conversation",
      corps: "(elle ne répond plus)"
    },

    blocage: {
      titre: "🔴 Confiance perdue",
      ines:  "Je t'avais dit que je savais pas si je pouvais te faire confiance.",
      sys:   "(elle ne répond plus)"
    },

    succes: {
      titre: "🟢 Inès te fait confiance",
      dialogue: [
        { who: 'Inès', t: "Tu promets de faire attention à ce que tu lis ?" },
        { who: 'Léo',  t: "Je promets." },
        { who: 'Inès', t: "Et tu me dis si tu trouves quelque chose." },
        { who: 'Inès', t: "Elle me l'avait donné au cas où. Tu l'utilises, t'en parles à personne.", gap: true }
      ],
      ig: {
        label:       "📱 Instagram de Clara",
        compteLabel: "compte :",
        compte:      "@clara.fontaine",
        mdpLabel:    "mdp :",
        mdp:         "nuit_rouge17",
        warn:        "⚠ C'est sa vie privée. Respecte-la."
      }
    },

    fragile: {
      titre: "🟡 Succès fragile",
      dialogue: [
        { who: 'Inès', t: "Je sais vraiment pas si je fais bien.\nTu me promets de faire attention ?" },
        { who: 'Léo',  t: "Oui." }
      ],
      ig: {
        label:       "📱 Instagram de Clara",
        compteLabel: "compte :",
        compte:      "@clara.fontaine",
        mdpLabel:    "mdp :",
        mdp:         "nuit_rouge17",
        warn:        "⚠ Sois prudent."
      }
    },

    echec: {
      titre: "🔴 Échec",
      ines:  "Non.\nArrête de fouiller.\nC'est pas tes affaires.",
      sys:   "(elle ne répond plus)"
    }

  }

};
