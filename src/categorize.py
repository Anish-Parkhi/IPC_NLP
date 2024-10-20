def categorize_article(text, ipc_sections):
    
    matched_sections = []
    for section, keywords in ipc_sections.items():
        if any(keyword in text for keyword in keywords):
            matched_sections.append(section)
    if matched_sections:
        return matched_sections
    # IPC section 
    return ['IPC 511']

# return categorize_article 


ipc_sections = {
    'IPC 302': ['murder', 'homicide', 'kill'],
    'IPC 307': ['attempt to murder', 'assassination attempt', 'murder attempt'],
    'IPC 304': ['culpable homicide', 'negligence', 'manslaughter'],
    'IPC 324': ['voluntarily causing hurt', 'physical assault', 'wounding'],
    'IPC 325': ['grievous hurt', 'severe injury', 'serious harm'],
    'IPC 354': ['outraging modesty', 'molestation', 'sexual harassment'],
    'IPC 376': ['rape', 'sexual assault', 'molestation'],
    'IPC 377': ['unnatural offences', 'homosexuality', 'sodomy'],
    'IPC 392': ['robbery', 'theft by force', 'armed robbery'],
    'IPC 395': ['dacoity', 'gang robbery', 'armed theft'],
    'IPC 420': ['fraud', 'deception', 'scam'],
    'IPC 498A': ['domestic violence', 'cruelty', 'marital abuse'],
    'IPC 506': ['criminal intimidation', 'threats', 'harassment'],
    'IPC 509': ['insult to modesty of a woman', 'verbal abuse', 'insult'],
    'IPC 120B': ['criminal conspiracy', 'collusion', 'plotting'],
    'IPC 201': ['causing disappearance of evidence', 'destroying evidence', 'tampering'],
    'IPC 141': ['unlawful assembly', 'riot', 'mob violence'],
    'IPC 279': ['rash driving', 'negligent driving', 'reckless driving'],
    'IPC 304A': ['death by negligence', 'accidental death', 'careless action'],
    'IPC 336': ['endangering life', 'negligent act', 'reckless behavior'],
    'IPC 338': ['causing grievous hurt by act endangering life', 'serious injury', 'dangerous negligence'],
    'IPC 295A': ['deliberate insult to religion', 'hurting religious sentiments', 'blasphemy'],
    'IPC 153A': ['promoting enmity between groups', 'hate speech', 'incitement'],
    'IPC 505': ['public mischief', 'false statements', 'rumors'],
    'IPC 467': ['forgery', 'falsifying documents', 'document fraud'],
    'IPC 468': ['forgery for cheating', 'fraudulent forgery', 'document manipulation'],
    'IPC 471': ['using forged documents', 'fake document use', 'forged papers'],
    'IPC 489A': ['counterfeiting currency', 'fake currency', 'money forgery'],
    'IPC 34': ['acts done by several persons', 'common intention', 'joint liability'],
    'IPC 120A': ['criminal conspiracy', 'plotting', 'collusion for crime'],
    'IPC 153B': ['imputations prejudicial to national integration', 'anti-national speech', 'seditious speech'],
    'IPC 304B': ['dowry death', 'bride death due to dowry', 'dowry-related violence'],
    'IPC 363': ['kidnapping', 'abduction', 'illegal confinement'],
    'IPC 370': ['trafficking', 'human trafficking', 'forced labor'],
    'IPC 379': ['theft', 'stealing', 'robbery'],
    'IPC 403': ['dishonest misappropriation of property', 'embezzlement', 'unlawful possession'],
}
