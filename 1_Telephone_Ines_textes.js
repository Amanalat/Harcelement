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
    "elle ne te fait plus confiance",
    "elle est très méfiante",
    "elle est méfiante",
    "elle hésite",
    "elle t'écoute",
    "elle t'écoute bien",
    "elle te fait confiance",
    "elle te fait confiance",
    "elle te fait vraiment confiance"
  ],
  trustInitial: "elle hésite",

  choiceHint:       "Que répond Léo ?",
  choiceHintCrise:  "Comment réagit Léo ?",
  restartBtn:       "↺ Recommencer",
  revelationsHeader:"📋 CE QUE TU AS APPRIS SUR CLARA",

  // ─── Séquence d'ouverture ─────────────────────────────────────────────────

  ouverture: [
    { t: "Hey… Inès ?",                                                type: 's' },
    { t: "Oui, c'est qui ?",                                           type: 'r' },
    { t: "C'est Léo. Un ami de Clara.",                                type: 's' },
    { t: "Léo… (pause) On s'est jamais vraiment parlé.",               type: 'r' },
    { t: "Je sais. Mais Clara a disparu. J'arrive plus à la joindre.", type: 's' },
    { t: "…Pourquoi tu m'appelles, moi ?",                             type: 'r' }
  ],

  // ─── Messages de fin rapide / blocage ────────────────────────────────────

  finImmediate: [
    { t: "…ok",   type: 'r'  },
    { t: "vu ✔️", type: 'sy' }
  ],

  blocageMessages: [
    { t: "Non.",                 type: 'cr' },
    { t: "Arrête de me parler.", type: 'cr' },
    { t: "(elle te bloque)",     type: 'sy' }
  ],

  // ─── Révélations (résumé de ce qu'on apprend sur Clara) ──────────────────

  REVELATIONS: [
    {
      icon:  '💬',
      title: 'Groupe de moqueries en ligne',
      txt:   "Des élèves ont créé un groupe secret pour se moquer de Clara collectivement. Elle l'a appris par une capture d'écran."
    },
    {
      icon:  '👻',
      title: 'Harcèlement anonyme, la nuit',
      txt:   "Des comptes sans identité l'harcelaient chez elle, la nuit. Ne pas pouvoir identifier l'agresseur rendait l'angoisse permanente."
    },
    {
      icon:  '📊',
      title: "Sondage d'humiliation publique",
      txt:   "Un sondage la ciblant directement a circulé dans toute la classe. Clara l'a vu. Elle a fini par intégrer ce regard comme une vérité sur elle-même."
    }
  ],

  // ─── Scénario principal (G) ───────────────────────────────────────────────
  // Chaque étape peut avoir : intro (tableau de répliques), edu (note pédagogique), c (choix A/B/C)
  // e = effet sur la confiance : +1 bon, -1 mauvais, 0 neutre

  G: [

    // Étape 0 — Premier contact : pourquoi Léo appelle
    {
      c: [
        { l: 'A', t: "Parce qu'elle a disparu et que personne ne réagit.", e:  1 },
        { l: 'B', t: "T'es sa meilleure amie, t'as forcément des infos.",  e: -1 },
        { l: 'C', t: "Je suis inquiet, c'est tout.",                       e:  0 }
      ]
    },

    // Étape 1 — Le groupe de moqueries
    {
      intro: [
        "Pourquoi tu t'en mêles, toi ? Je te connais même pas.",
        "…",
        "(voix plus basse) Des gens de la classe ont créé un groupe. Pour parler d'elle. En se moquant.",
        "Elle l'a su par hasard. Quelqu'un lui a envoyé une capture."
      ],
      edu: "💡 Le cyberharcèlement en groupe : quand une communauté en ligne cible une personne, l'humiliation devient collective. La victime se retrouve seule face à tous, sans pouvoir se défendre.",
      c: [
        { l: 'A', t: "C'est du harcèlement en groupe. Elle a dû se sentir complètement seule face à tout ça.", e:  1 },
        { l: 'B', t: "Qui a fait ça ? Donne-moi les noms.",                                                    e: -1 },
        { l: 'C', t: "Ça arrive souvent ce genre de trucs…",                                                    e:  0 }
      ]
    },

    // Étape 2 — Les messages anonymes nocturnes
    {
      intro: [
        "C'était pas que ça.",
        "(silence) Elle recevait des messages la nuit. Des comptes sans nom, sans visage.",
        "Elle savait pas qui c'était. Elle pouvait pas se défendre.",
        "Elle éteignait son téléphone… mais après elle avait peur de le rallumer."
      ],
      edu: "💡 L'anonymat amplifie le harcèlement : sans visage, sans identité, la victime ne sait pas d'où vient l'attaque. Le refuge chez soi n'existe plus — l'angoisse est constante.",
      c: [
        { l: 'A', t: "Ne pas savoir qui envoie ces messages, c'est encore plus difficile à supporter.", e:  1 },
        { l: 'B', t: "Elle aurait pu désactiver ses réseaux.",                                           e: -1 },
        { l: 'C', t: "C'est grave. Elle en a parlé à quelqu'un ?",                                       e:  0 }
      ]
    },

    // Étape 3 — Le sondage d'humiliation
    {
      intro: [
        "(longue pause)",
        "…Il y a eu un sondage. Partagé dans toute la classe.",
        "« Clara est-elle la personne la plus nulle du collège ? »",
        "Les gens ont voté. Publiquement.",
        "Elle l'a vu."
      ],
      edu: "💡 Le vote d'humiliation : transformer une personne en objet d'un jugement public collectif. Avec le temps, la victime finit par intégrer ce regard comme une vérité sur elle-même.",
      c: [
        { l: 'A', t: "Une humiliation publique comme ça, ça touche à l'image qu'on a de soi. Elle a dû finir par y croire.", e: 1 },
        { l: 'B', t: "C'est illégal. Il faut le signaler à l'école.",                                                        e: 0 },
        { l: 'C', t: "Les gens peuvent être vraiment cruels.",                                                               e: 0 }
      ]
    },

    // Étape 4 — Pourquoi elle est partie + accès Instagram
    {
      intro: [
        "(longtemps sans répondre)",
        "Elle pouvait plus y échapper. Ni au collège. Ni chez elle.",
        "Son téléphone était devenu une source de peur.",
        "(silence) C'est pas à moi de tout te raconter.",
        "Mais… il y a peut-être des choses sur son Instagram. Un message, une photo, un endroit mentionné.",
        "Clara me l'avait donné au cas où. Mais je sais pas si je devrais te le donner."
      ],
      c: [
        { l: 'A', t: "Je comprends que c'est sa vie privée. T'as le droit de pas me le donner.",  e:  1 },
        { l: 'B', t: "Donne-le moi, je trouverai ce qu'il faut peu importe comment.",              e: -1 },
        { l: 'C', t: "C'est toi qui décides. Moi je veux juste la retrouver.",                     e:  0 }
      ]
    }

  ],

  // ─── Crise de confiance ───────────────────────────────────────────────────

  CRISIS: {
    intro: [
      "…",
      "Attends.",
      "T'es là pour quoi exactement ?",
      "J'ai pas confiance en toi."
    ],
    c: [
      { l: 'A', t: "T'as aucune raison de me faire confiance. Je te demande rien, je veux juste que Clara aille bien.", e:  2 },
      { l: 'B', t: "Ok. Je te force à rien. On peut en rester là si tu veux.",                                          e:  0 },
      { l: 'C', t: "Mais fais-moi confiance, j'essaie juste d'aider !",                                                 e: -1 }
    ]
  },

  // ─── Fins ─────────────────────────────────────────────────────────────────

  fins: {

    imm: {
      titre: "Fin immédiate",
      corps: "(fin de la conversation)"
    },

    blocage: {
      titre: "🔴 Confiance brisée",
      ines:  "Je t'avais prévenu.",
      sys:   "(elle te bloque)"
    },

    succes: {
      titre: "🟢 Inès te fait confiance",
      // gap:true = saut de ligne supplémentaire avant la réplique
      dialogue: [
        { who: 'Inès', t: "…Tu promets de faire attention à ce que tu lis ?" },
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
      // \n à l'intérieur d'une réplique = même locuteur, retour à la ligne
      dialogue: [
        { who: 'Inès', t: "Je sais vraiment pas si je fais bien…\nTu me promets de faire attention ?" },
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
      ines: "Non.\nArrête de fouiller.\nC'est pas tes affaires.",
      sys:  "(elle ne répond plus)"
    }

  }

};
