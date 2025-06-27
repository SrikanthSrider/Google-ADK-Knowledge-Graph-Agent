# Relationship Types & Properties

## ARRESTED_FOR
- date: Date arrested  
- location: Place of arrest  
- allegation: Brief description of alleged crime

## CHARGED_WITH
- date: Date charges filed  
- charge_type: Legal classification of charge

## CONVICTED_OF
- date: Date of conviction  
- method: "verdict" or "plea"

## RECEIVED_PENALTY_FOR
- jail_months: Number of months incarcerated  
- fine_amount: Monetary amount received  
- currency: Currency unit  
- reason: Explanation for penalty  
- death_penalty: Boolean (if capital punishment)

## VIOLATED
- law: Name of regulation/statute  
- date: Date violation occurred  
- violation_detail: Specific breach information

## INVESTIGATED_BY
- authority: Investigating body (e.g., "FBI")  
- start_date: Investigation start date  
- end_date: Investigation end date

## ISSUED_WARRANT_FOR
- warrant_type: Type (e.g., extradition, arrest)  
- date: Issue date  
- authority: Issuing authority

## WARNING_FROM
- authority: Source of warning  
- date: Warning date  
- reason: Rationale behind warning

## SANCTIONED_BY
- authority: Sanctioning body  
- date: Sanctions effective date  
- type: Category of sanction ("asset_freeze", "travel_ban", etc.)  
- details: Additional notes

## VISITED
- date: Visit dates (start–end)  
- purpose: Reason for visit  
- hosts: Host information

## LEGAL_ACTION_AGAINST
- action_type: Type of action (e.g., "seizure", "injunction")  
- authority: Enforcing body  
- date: Action date

## CALLED_ELECTION
- date: Election announcement date  
- level: "national", "local", etc.  
- subject: Body or person initiating

## WON_ELECTION
- date: Election date  
- position: Title/office obtained

## POLITICAL_OUTCOME
- motion: Name of parliamentary motion  
- result: "passed" or "failed"  
- date: Decision date

## FLED_TO
- destination: Country/region relocated to  
- date: Relocation date  
- reason: Reason for fleeing

## ASSOCIATED_WITH
- relationship_type: e.g., "partner", "collaborator"  
- since_date: Start date of association
