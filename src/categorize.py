def categorize_article(text, ipc_sections):
    for section, keywords in ipc_sections.items():
        if any(keyword in text for keyword in keywords):
            return section
    return 'Uncategorized'

ipc_sections = {
    'IPC 302': ['murder', 'homicide', 'kill'],
    'IPC 420': ['fraud', 'deception', 'scam'],
    'IPC 376': ['rape', 'sexual assault'],
}
