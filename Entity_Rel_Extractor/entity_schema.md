# Entity Types & Properties

## Person
- id: Unique identifier  
- name: Full name  
- birth_date: Date or year  
- nationality: Country code  
- occupation: Job or role (optional)

## Organization
- id: Unique identifier  
- name: Organization name  
- type: e.g., "Bank", "Government Agency"  
- location: HQ location

## Country
- code: ISO country code  
- name: Country name  
- region: Optional region tag

## LegalCase (optional)
- id: Unique identifier  
- title: Case name  
- jurisdiction: Legal area  
- start_date: Commencement date  
- end_date: Conclusion date  
- case_number: Official reference

## Law
- id: Unique identifier  
- name: Law/regulation title  
- jurisdiction: Region where enforceable  
- effective_date: Date enacted

## Crime
- id: Unique identifier  
- name: Crime name  
- category: e.g., "violent", "financial", "drug"

## Election/Event
- id: Unique identifier  
- name: Event name  
- type: e.g., "legislative", "vote_of_confidence"  
- date: Event date
