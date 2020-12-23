from typing import Union

from .FHIR_Account import FHIR_Account
from .FHIR_ActivityDefinition import FHIR_ActivityDefinition
from .FHIR_AdverseEvent import FHIR_AdverseEvent
from .FHIR_AllergyIntolerance import FHIR_AllergyIntolerance
from .FHIR_Appointment import FHIR_Appointment
from .FHIR_AppointmentResponse import FHIR_AppointmentResponse
from .FHIR_AuditEvent import FHIR_AuditEvent
from .FHIR_Basic import FHIR_Basic
from .FHIR_Binary import FHIR_Binary
from .FHIR_BiologicallyDerivedProduct import FHIR_BiologicallyDerivedProduct
from .FHIR_BodyStructure import FHIR_BodyStructure
from .FHIR_Bundle import FHIR_Bundle
from .FHIR_CapabilityStatement import FHIR_CapabilityStatement
from .FHIR_CarePlan import FHIR_CarePlan
from .FHIR_CareTeam import FHIR_CareTeam
from .FHIR_CatalogEntry import FHIR_CatalogEntry
from .FHIR_ChargeItem import FHIR_ChargeItem
from .FHIR_ChargeItemDefinition import FHIR_ChargeItemDefinition
from .FHIR_Claim import FHIR_Claim
from .FHIR_ClaimResponse import FHIR_ClaimResponse
from .FHIR_ClinicalImpression import FHIR_ClinicalImpression
from .FHIR_CodeSystem import FHIR_CodeSystem
from .FHIR_Communication import FHIR_Communication
from .FHIR_CommunicationRequest import FHIR_CommunicationRequest
from .FHIR_CompartmentDefinition import FHIR_CompartmentDefinition
from .FHIR_Composition import FHIR_Composition
from .FHIR_ConceptMap import FHIR_ConceptMap
from .FHIR_Condition import FHIR_Condition
from .FHIR_Consent import FHIR_Consent
from .FHIR_Contract import FHIR_Contract
from .FHIR_Coverage import FHIR_Coverage
from .FHIR_CoverageEligibilityRequest import FHIR_CoverageEligibilityRequest
from .FHIR_CoverageEligibilityResponse import FHIR_CoverageEligibilityResponse
from .FHIR_DetectedIssue import FHIR_DetectedIssue
from .FHIR_Device import FHIR_Device
from .FHIR_DeviceDefinition import FHIR_DeviceDefinition
from .FHIR_DeviceMetric import FHIR_DeviceMetric
from .FHIR_DeviceRequest import FHIR_DeviceRequest
from .FHIR_DeviceUseStatement import FHIR_DeviceUseStatement
from .FHIR_DiagnosticReport import FHIR_DiagnosticReport
from .FHIR_DocumentManifest import FHIR_DocumentManifest
from .FHIR_DocumentReference import FHIR_DocumentReference
from .FHIR_EffectEvidenceSynthesis import FHIR_EffectEvidenceSynthesis
from .FHIR_Encounter import FHIR_Encounter
from .FHIR_Endpoint import FHIR_Endpoint
from .FHIR_EnrollmentRequest import FHIR_EnrollmentRequest
from .FHIR_EnrollmentResponse import FHIR_EnrollmentResponse
from .FHIR_EpisodeOfCare import FHIR_EpisodeOfCare
from .FHIR_EventDefinition import FHIR_EventDefinition
from .FHIR_Evidence import FHIR_Evidence
from .FHIR_EvidenceVariable import FHIR_EvidenceVariable
from .FHIR_ExampleScenario import FHIR_ExampleScenario
from .FHIR_ExplanationOfBenefit import FHIR_ExplanationOfBenefit
from .FHIR_FamilyMemberHistory import FHIR_FamilyMemberHistory
from .FHIR_Flag import FHIR_Flag
from .FHIR_Goal import FHIR_Goal
from .FHIR_GraphDefinition import FHIR_GraphDefinition
from .FHIR_Group import FHIR_Group
from .FHIR_GuidanceResponse import FHIR_GuidanceResponse
from .FHIR_HealthcareService import FHIR_HealthcareService
from .FHIR_ImagingStudy import FHIR_ImagingStudy
from .FHIR_Immunization import FHIR_Immunization
from .FHIR_ImmunizationEvaluation import FHIR_ImmunizationEvaluation
from .FHIR_ImmunizationRecommendation import FHIR_ImmunizationRecommendation
from .FHIR_ImplementationGuide import FHIR_ImplementationGuide
from .FHIR_InsurancePlan import FHIR_InsurancePlan
from .FHIR_Invoice import FHIR_Invoice
from .FHIR_Library import FHIR_Library
from .FHIR_Linkage import FHIR_Linkage
from .FHIR_List import FHIR_List
from .FHIR_Location import FHIR_Location
from .FHIR_Measure import FHIR_Measure
from .FHIR_MeasureReport import FHIR_MeasureReport
from .FHIR_Media import FHIR_Media
from .FHIR_Medication import FHIR_Medication
from .FHIR_MedicationAdministration import FHIR_MedicationAdministration
from .FHIR_MedicationDispense import FHIR_MedicationDispense
from .FHIR_MedicationKnowledge import FHIR_MedicationKnowledge
from .FHIR_MedicationRequest import FHIR_MedicationRequest
from .FHIR_MedicationStatement import FHIR_MedicationStatement
from .FHIR_MedicinalProduct import FHIR_MedicinalProduct
from .FHIR_MedicinalProductAuthorization import FHIR_MedicinalProductAuthorization
from .FHIR_MedicinalProductContraindication import FHIR_MedicinalProductContraindication
from .FHIR_MedicinalProductIndication import FHIR_MedicinalProductIndication
from .FHIR_MedicinalProductIngredient import FHIR_MedicinalProductIngredient
from .FHIR_MedicinalProductInteraction import FHIR_MedicinalProductInteraction
from .FHIR_MedicinalProductManufactured import FHIR_MedicinalProductManufactured
from .FHIR_MedicinalProductPackaged import FHIR_MedicinalProductPackaged
from .FHIR_MedicinalProductPharmaceutical import FHIR_MedicinalProductPharmaceutical
from .FHIR_MedicinalProductUndesirableEffect import (
    FHIR_MedicinalProductUndesirableEffect,
)
from .FHIR_MessageDefinition import FHIR_MessageDefinition
from .FHIR_MessageHeader import FHIR_MessageHeader
from .FHIR_MolecularSequence import FHIR_MolecularSequence
from .FHIR_NamingSystem import FHIR_NamingSystem
from .FHIR_NutritionOrder import FHIR_NutritionOrder
from .FHIR_Observation import FHIR_Observation
from .FHIR_ObservationDefinition import FHIR_ObservationDefinition
from .FHIR_OperationDefinition import FHIR_OperationDefinition
from .FHIR_OperationOutcome import FHIR_OperationOutcome
from .FHIR_Organization import FHIR_Organization
from .FHIR_OrganizationAffiliation import FHIR_OrganizationAffiliation
from .FHIR_Parameters import FHIR_Parameters
from .FHIR_Patient import FHIR_Patient
from .FHIR_PaymentNotice import FHIR_PaymentNotice
from .FHIR_PaymentReconciliation import FHIR_PaymentReconciliation
from .FHIR_Person import FHIR_Person
from .FHIR_PlanDefinition import FHIR_PlanDefinition
from .FHIR_Practitioner import FHIR_Practitioner
from .FHIR_PractitionerRole import FHIR_PractitionerRole
from .FHIR_Procedure import FHIR_Procedure
from .FHIR_Provenance import FHIR_Provenance
from .FHIR_Questionnaire import FHIR_Questionnaire
from .FHIR_QuestionnaireResponse import FHIR_QuestionnaireResponse
from .FHIR_RelatedPerson import FHIR_RelatedPerson
from .FHIR_RequestGroup import FHIR_RequestGroup
from .FHIR_ResearchDefinition import FHIR_ResearchDefinition
from .FHIR_ResearchElementDefinition import FHIR_ResearchElementDefinition
from .FHIR_ResearchStudy import FHIR_ResearchStudy
from .FHIR_ResearchSubject import FHIR_ResearchSubject
from .FHIR_RiskAssessment import FHIR_RiskAssessment
from .FHIR_RiskEvidenceSynthesis import FHIR_RiskEvidenceSynthesis
from .FHIR_Schedule import FHIR_Schedule
from .FHIR_SearchParameter import FHIR_SearchParameter
from .FHIR_ServiceRequest import FHIR_ServiceRequest
from .FHIR_Slot import FHIR_Slot
from .FHIR_Specimen import FHIR_Specimen
from .FHIR_SpecimenDefinition import FHIR_SpecimenDefinition
from .FHIR_StructureDefinition import FHIR_StructureDefinition
from .FHIR_StructureMap import FHIR_StructureMap
from .FHIR_Subscription import FHIR_Subscription
from .FHIR_Substance import FHIR_Substance
from .FHIR_SubstanceNucleicAcid import FHIR_SubstanceNucleicAcid
from .FHIR_SubstancePolymer import FHIR_SubstancePolymer
from .FHIR_SubstanceProtein import FHIR_SubstanceProtein
from .FHIR_SubstanceReferenceInformation import FHIR_SubstanceReferenceInformation
from .FHIR_SubstanceSourceMaterial import FHIR_SubstanceSourceMaterial
from .FHIR_SubstanceSpecification import FHIR_SubstanceSpecification
from .FHIR_SupplyDelivery import FHIR_SupplyDelivery
from .FHIR_SupplyRequest import FHIR_SupplyRequest
from .FHIR_Task import FHIR_Task
from .FHIR_TerminologyCapabilities import FHIR_TerminologyCapabilities
from .FHIR_TestReport import FHIR_TestReport
from .FHIR_TestScript import FHIR_TestScript
from .FHIR_ValueSet import FHIR_ValueSet
from .FHIR_VerificationResult import FHIR_VerificationResult
from .FHIR_VisionPrescription import FHIR_VisionPrescription

FHIR_ResourceList = Union[
    FHIR_Account,
    FHIR_ActivityDefinition,
    FHIR_AdverseEvent,
    FHIR_AllergyIntolerance,
    FHIR_Appointment,
    FHIR_AppointmentResponse,
    FHIR_AuditEvent,
    FHIR_Basic,
    FHIR_Binary,
    FHIR_BiologicallyDerivedProduct,
    FHIR_BodyStructure,
    FHIR_Bundle,
    FHIR_CapabilityStatement,
    FHIR_CarePlan,
    FHIR_CareTeam,
    FHIR_CatalogEntry,
    FHIR_ChargeItem,
    FHIR_ChargeItemDefinition,
    FHIR_Claim,
    FHIR_ClaimResponse,
    FHIR_ClinicalImpression,
    FHIR_CodeSystem,
    FHIR_Communication,
    FHIR_CommunicationRequest,
    FHIR_CompartmentDefinition,
    FHIR_Composition,
    FHIR_ConceptMap,
    FHIR_Condition,
    FHIR_Consent,
    FHIR_Contract,
    FHIR_Coverage,
    FHIR_CoverageEligibilityRequest,
    FHIR_CoverageEligibilityResponse,
    FHIR_DetectedIssue,
    FHIR_Device,
    FHIR_DeviceDefinition,
    FHIR_DeviceMetric,
    FHIR_DeviceRequest,
    FHIR_DeviceUseStatement,
    FHIR_DiagnosticReport,
    FHIR_DocumentManifest,
    FHIR_DocumentReference,
    FHIR_EffectEvidenceSynthesis,
    FHIR_Encounter,
    FHIR_Endpoint,
    FHIR_EnrollmentRequest,
    FHIR_EnrollmentResponse,
    FHIR_EpisodeOfCare,
    FHIR_EventDefinition,
    FHIR_Evidence,
    FHIR_EvidenceVariable,
    FHIR_ExampleScenario,
    FHIR_ExplanationOfBenefit,
    FHIR_FamilyMemberHistory,
    FHIR_Flag,
    FHIR_Goal,
    FHIR_GraphDefinition,
    FHIR_Group,
    FHIR_GuidanceResponse,
    FHIR_HealthcareService,
    FHIR_ImagingStudy,
    FHIR_Immunization,
    FHIR_ImmunizationEvaluation,
    FHIR_ImmunizationRecommendation,
    FHIR_ImplementationGuide,
    FHIR_InsurancePlan,
    FHIR_Invoice,
    FHIR_Library,
    FHIR_Linkage,
    FHIR_List,
    FHIR_Location,
    FHIR_Measure,
    FHIR_MeasureReport,
    FHIR_Media,
    FHIR_Medication,
    FHIR_MedicationAdministration,
    FHIR_MedicationDispense,
    FHIR_MedicationKnowledge,
    FHIR_MedicationRequest,
    FHIR_MedicationStatement,
    FHIR_MedicinalProduct,
    FHIR_MedicinalProductAuthorization,
    FHIR_MedicinalProductContraindication,
    FHIR_MedicinalProductIndication,
    FHIR_MedicinalProductIngredient,
    FHIR_MedicinalProductInteraction,
    FHIR_MedicinalProductManufactured,
    FHIR_MedicinalProductPackaged,
    FHIR_MedicinalProductPharmaceutical,
    FHIR_MedicinalProductUndesirableEffect,
    FHIR_MessageDefinition,
    FHIR_MessageHeader,
    FHIR_MolecularSequence,
    FHIR_NamingSystem,
    FHIR_NutritionOrder,
    FHIR_Observation,
    FHIR_ObservationDefinition,
    FHIR_OperationDefinition,
    FHIR_OperationOutcome,
    FHIR_Organization,
    FHIR_OrganizationAffiliation,
    FHIR_Parameters,
    FHIR_Patient,
    FHIR_PaymentNotice,
    FHIR_PaymentReconciliation,
    FHIR_Person,
    FHIR_PlanDefinition,
    FHIR_Practitioner,
    FHIR_PractitionerRole,
    FHIR_Procedure,
    FHIR_Provenance,
    FHIR_Questionnaire,
    FHIR_QuestionnaireResponse,
    FHIR_RelatedPerson,
    FHIR_RequestGroup,
    FHIR_ResearchDefinition,
    FHIR_ResearchElementDefinition,
    FHIR_ResearchStudy,
    FHIR_ResearchSubject,
    FHIR_RiskAssessment,
    FHIR_RiskEvidenceSynthesis,
    FHIR_Schedule,
    FHIR_SearchParameter,
    FHIR_ServiceRequest,
    FHIR_Slot,
    FHIR_Specimen,
    FHIR_SpecimenDefinition,
    FHIR_StructureDefinition,
    FHIR_StructureMap,
    FHIR_Subscription,
    FHIR_Substance,
    FHIR_SubstanceNucleicAcid,
    FHIR_SubstancePolymer,
    FHIR_SubstanceProtein,
    FHIR_SubstanceReferenceInformation,
    FHIR_SubstanceSourceMaterial,
    FHIR_SubstanceSpecification,
    FHIR_SupplyDelivery,
    FHIR_SupplyRequest,
    FHIR_Task,
    FHIR_TerminologyCapabilities,
    FHIR_TestReport,
    FHIR_TestScript,
    FHIR_ValueSet,
    FHIR_VerificationResult,
    FHIR_VisionPrescription,
]
