#!/usr/bin/env/python

import enum


class InertLandfill:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class ContactAgent:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class ConsentRegimes:

    _types_map = {
        'consentRegime': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, consentRegime=None
                 ):
        self.__consentRegime = consentRegime

    def _get_consentRegime(self):
        return self.__consentRegime

    def _set_consentRegime(self, value):
        if not isinstance(value, list):
            raise TypeError("consentRegime must be list")
        self.__consentRegime = value
    consentRegime = property(_get_consentRegime, _set_consentRegime)

    def as_dict(self):
        d = dict()
        if self.__consentRegime is not None:
            d['consentRegime'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__consentRegime]
        return d


class Boundaries:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        'proposed': {'type': list, 'subtype': None},
        'notApplicable': {'type': list, 'subtype': None},
        'dontKnow': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, proposed=None, notApplicable=None, dontKnow=None
                 ):
        self.__existing = existing
        self.__proposed = proposed
        self.__notApplicable = notApplicable
        self.__dontKnow = dontKnow

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get_proposed(self):
        return self.__proposed

    def _set_proposed(self, value):
        if not isinstance(value, list):
            raise TypeError("proposed must be list")
        self.__proposed = value
    proposed = property(_get_proposed, _set_proposed)

    def _get_notApplicable(self):
        return self.__notApplicable

    def _set_notApplicable(self, value):
        if not isinstance(value, list):
            raise TypeError("notApplicable must be list")
        self.__notApplicable = value
    notApplicable = property(_get_notApplicable, _set_notApplicable)

    def _get_dontKnow(self):
        return self.__dontKnow

    def _set_dontKnow(self, value):
        if not isinstance(value, list):
            raise TypeError("dontKnow must be list")
        self.__dontKnow = value
    dontKnow = property(_get_dontKnow, _set_dontKnow)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.__proposed is not None:
            d['proposed'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__proposed]
        if self.__notApplicable is not None:
            d['notApplicable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__notApplicable]
        if self.__dontKnow is not None:
            d['dontKnow'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dontKnow]
        return d


class WasteStorageCollection:

    _types_map = {
        'storeCollectWaste': {'type': list, 'subtype': None},
        'storeCollectRecyclableWaste': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, storeCollectWaste=None, storeCollectRecyclableWaste=None
                 ):
        self.__storeCollectWaste = storeCollectWaste
        self.__storeCollectRecyclableWaste = storeCollectRecyclableWaste

    def _get_storeCollectWaste(self):
        return self.__storeCollectWaste

    def _set_storeCollectWaste(self, value):
        if not isinstance(value, list):
            raise TypeError("storeCollectWaste must be list")
        self.__storeCollectWaste = value
    storeCollectWaste = property(_get_storeCollectWaste, _set_storeCollectWaste)

    def _get_storeCollectRecyclableWaste(self):
        return self.__storeCollectRecyclableWaste

    def _set_storeCollectRecyclableWaste(self, value):
        if not isinstance(value, list):
            raise TypeError("storeCollectRecyclableWaste must be list")
        self.__storeCollectRecyclableWaste = value
    storeCollectRecyclableWaste = property(
        _get_storeCollectRecyclableWaste, _set_storeCollectRecyclableWaste)

    def as_dict(self):
        d = dict()
        if self.__storeCollectWaste is not None:
            d['storeCollectWaste'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__storeCollectWaste]
        if self.__storeCollectRecyclableWaste is not None:
            d['storeCollectRecyclableWaste'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__storeCollectRecyclableWaste]
        return d


class LandfillGasGenerationPlant:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class C1:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
        'roomInformation': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None, roomInformation=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace
        self.__roomInformation = roomInformation

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def _get_roomInformation(self):
        return self.__roomInformation

    def _set_roomInformation(self, value):
        if not isinstance(value, list):
            raise TypeError("roomInformation must be list")
        self.__roomInformation = value
    roomInformation = property(_get_roomInformation, _set_roomInformation)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        if self.__roomInformation is not None:
            d['roomInformation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__roomInformation]
        return d


class FileAttachment:

    _types_map = {
        'identifier': {'type': list, 'subtype': None},
        'size': {'type': list, 'subtype': None},
        'mimeType': {'type': list, 'subtype': None},
        'fileName': {'type': list, 'subtype': None},
        'printInformation': {'type': list, 'subtype': None},
        'reference': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, identifier=None, size=None, mimeType=None, fileName=None, printInformation=None, reference=None
                 ):
        self.__identifier = identifier
        self.__size = size
        self.__mimeType = mimeType
        self.__fileName = fileName
        self.__printInformation = printInformation
        self.__reference = reference

    def _get_identifier(self):
        return self.__identifier

    def _set_identifier(self, value):
        if not isinstance(value, list):
            raise TypeError("identifier must be list")
        self.__identifier = value
    identifier = property(_get_identifier, _set_identifier)

    def _get_size(self):
        return self.__size

    def _set_size(self, value):
        if not isinstance(value, list):
            raise TypeError("size must be list")
        self.__size = value
    size = property(_get_size, _set_size)

    def _get_mimeType(self):
        return self.__mimeType

    def _set_mimeType(self, value):
        if not isinstance(value, list):
            raise TypeError("mimeType must be list")
        self.__mimeType = value
    mimeType = property(_get_mimeType, _set_mimeType)

    def _get_fileName(self):
        return self.__fileName

    def _set_fileName(self, value):
        if not isinstance(value, list):
            raise TypeError("fileName must be list")
        self.__fileName = value
    fileName = property(_get_fileName, _set_fileName)

    def _get_printInformation(self):
        return self.__printInformation

    def _set_printInformation(self, value):
        if not isinstance(value, list):
            raise TypeError("printInformation must be list")
        self.__printInformation = value
    printInformation = property(_get_printInformation, _set_printInformation)

    def _get_reference(self):
        return self.__reference

    def _set_reference(self, value):
        if not isinstance(value, list):
            raise TypeError("reference must be list")
        self.__reference = value
    reference = property(_get_reference, _set_reference)

    def as_dict(self):
        d = dict()
        if self.__identifier is not None:
            d['identifier'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__identifier]
        if self.__size is not None:
            d['size'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__size]
        if self.__mimeType is not None:
            d['mimeType'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__mimeType]
        if self.__fileName is not None:
            d['fileName'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__fileName]
        if self.__printInformation is not None:
            d['printInformation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__printInformation]
        if self.__reference is not None:
            d['reference'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__reference]
        return d


class NoticeRecipientPerson:

    _types_map = {
        'personFamilyName': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, personFamilyName=None
                 ):
        self.__personFamilyName = personFamilyName

    def _get_personFamilyName(self):
        return self.__personFamilyName

    def _set_personFamilyName(self, value):
        if not isinstance(value, list):
            raise TypeError("personFamilyName must be list")
        self.__personFamilyName = value
    personFamilyName = property(_get_personFamilyName, _set_personFamilyName)

    def as_dict(self):
        d = dict()
        if self.__personFamilyName is not None:
            d['personFamilyName'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__personFamilyName]
        return d


class NoticeRecipientAddress:

    _types_map = {
        'paon': {'type': list, 'subtype': None},
        'streetDescription': {'type': list, 'subtype': None},
        'locality': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, paon=None, streetDescription=None, locality=None
                 ):
        self.__paon = paon
        self.__streetDescription = streetDescription
        self.__locality = locality

    def _get_paon(self):
        return self.__paon

    def _set_paon(self, value):
        if not isinstance(value, list):
            raise TypeError("paon must be list")
        self.__paon = value
    paon = property(_get_paon, _set_paon)

    def _get_streetDescription(self):
        return self.__streetDescription

    def _set_streetDescription(self, value):
        if not isinstance(value, list):
            raise TypeError("streetDescription must be list")
        self.__streetDescription = value
    streetDescription = property(_get_streetDescription, _set_streetDescription)

    def _get_locality(self):
        return self.__locality

    def _set_locality(self, value):
        if not isinstance(value, list):
            raise TypeError("locality must be list")
        self.__locality = value
    locality = property(_get_locality, _set_locality)

    def as_dict(self):
        d = dict()
        if self.__paon is not None:
            d['paon'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__paon]
        if self.__streetDescription is not None:
            d['streetDescription'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__streetDescription]
        if self.__locality is not None:
            d['locality'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__locality]
        return d


class NonResidentialDevelopment:

    _types_map = {
        'doesIncludeGainOrLoss': {'type': list, 'subtype': None},
        'a1': {'type': list, 'subtype': None},
        'a2': {'type': list, 'subtype': None},
        'a3': {'type': list, 'subtype': None},
        'a4': {'type': list, 'subtype': None},
        'a5': {'type': list, 'subtype': None},
        'b1A': {'type': list, 'subtype': None},
        'b1B': {'type': list, 'subtype': None},
        'b1C': {'type': list, 'subtype': None},
        'b2': {'type': list, 'subtype': None},
        'b8': {'type': list, 'subtype': None},
        'c1': {'type': list, 'subtype': None},
        'c2': {'type': list, 'subtype': None},
        'd1': {'type': list, 'subtype': None},
        'd2': {'type': list, 'subtype': None},
        'other': {'type': list, 'subtype': None},
        'totals': {'type': list, 'subtype': None},
        'areaUnit': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, doesIncludeGainOrLoss=None, a1=None, a2=None, a3=None, a4=None, a5=None, b1A=None, b1B=None, b1C=None, b2=None, b8=None, c1=None, c2=None, d1=None, d2=None, other=None, totals=None, areaUnit=None
                 ):
        self.__doesIncludeGainOrLoss = doesIncludeGainOrLoss
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__a5 = a5
        self.__b1A = b1A
        self.__b1B = b1B
        self.__b1C = b1C
        self.__b2 = b2
        self.__b8 = b8
        self.__c1 = c1
        self.__c2 = c2
        self.__d1 = d1
        self.__d2 = d2
        self.__other = other
        self.__totals = totals
        self.__areaUnit = areaUnit

    def _get_doesIncludeGainOrLoss(self):
        return self.__doesIncludeGainOrLoss

    def _set_doesIncludeGainOrLoss(self, value):
        if not isinstance(value, list):
            raise TypeError("doesIncludeGainOrLoss must be list")
        self.__doesIncludeGainOrLoss = value
    doesIncludeGainOrLoss = property(_get_doesIncludeGainOrLoss, _set_doesIncludeGainOrLoss)

    def _get_a1(self):
        return self.__a1

    def _set_a1(self, value):
        if not isinstance(value, list):
            raise TypeError("a1 must be list")
        self.__a1 = value
    a1 = property(_get_a1, _set_a1)

    def _get_a2(self):
        return self.__a2

    def _set_a2(self, value):
        if not isinstance(value, list):
            raise TypeError("a2 must be list")
        self.__a2 = value
    a2 = property(_get_a2, _set_a2)

    def _get_a3(self):
        return self.__a3

    def _set_a3(self, value):
        if not isinstance(value, list):
            raise TypeError("a3 must be list")
        self.__a3 = value
    a3 = property(_get_a3, _set_a3)

    def _get_a4(self):
        return self.__a4

    def _set_a4(self, value):
        if not isinstance(value, list):
            raise TypeError("a4 must be list")
        self.__a4 = value
    a4 = property(_get_a4, _set_a4)

    def _get_a5(self):
        return self.__a5

    def _set_a5(self, value):
        if not isinstance(value, list):
            raise TypeError("a5 must be list")
        self.__a5 = value
    a5 = property(_get_a5, _set_a5)

    def _get_b1A(self):
        return self.__b1A

    def _set_b1A(self, value):
        if not isinstance(value, list):
            raise TypeError("b1A must be list")
        self.__b1A = value
    b1A = property(_get_b1A, _set_b1A)

    def _get_b1B(self):
        return self.__b1B

    def _set_b1B(self, value):
        if not isinstance(value, list):
            raise TypeError("b1B must be list")
        self.__b1B = value
    b1B = property(_get_b1B, _set_b1B)

    def _get_b1C(self):
        return self.__b1C

    def _set_b1C(self, value):
        if not isinstance(value, list):
            raise TypeError("b1C must be list")
        self.__b1C = value
    b1C = property(_get_b1C, _set_b1C)

    def _get_b2(self):
        return self.__b2

    def _set_b2(self, value):
        if not isinstance(value, list):
            raise TypeError("b2 must be list")
        self.__b2 = value
    b2 = property(_get_b2, _set_b2)

    def _get_b8(self):
        return self.__b8

    def _set_b8(self, value):
        if not isinstance(value, list):
            raise TypeError("b8 must be list")
        self.__b8 = value
    b8 = property(_get_b8, _set_b8)

    def _get_c1(self):
        return self.__c1

    def _set_c1(self, value):
        if not isinstance(value, list):
            raise TypeError("c1 must be list")
        self.__c1 = value
    c1 = property(_get_c1, _set_c1)

    def _get_c2(self):
        return self.__c2

    def _set_c2(self, value):
        if not isinstance(value, list):
            raise TypeError("c2 must be list")
        self.__c2 = value
    c2 = property(_get_c2, _set_c2)

    def _get_d1(self):
        return self.__d1

    def _set_d1(self, value):
        if not isinstance(value, list):
            raise TypeError("d1 must be list")
        self.__d1 = value
    d1 = property(_get_d1, _set_d1)

    def _get_d2(self):
        return self.__d2

    def _set_d2(self, value):
        if not isinstance(value, list):
            raise TypeError("d2 must be list")
        self.__d2 = value
    d2 = property(_get_d2, _set_d2)

    def _get_other(self):
        return self.__other

    def _set_other(self, value):
        if not isinstance(value, list):
            raise TypeError("other must be list")
        self.__other = value
    other = property(_get_other, _set_other)

    def _get_totals(self):
        return self.__totals

    def _set_totals(self, value):
        if not isinstance(value, list):
            raise TypeError("totals must be list")
        self.__totals = value
    totals = property(_get_totals, _set_totals)

    def _get_areaUnit(self):
        return self.__areaUnit

    def _set_areaUnit(self, value):
        if not isinstance(value, list):
            raise TypeError("areaUnit must be list")
        self.__areaUnit = value
    areaUnit = property(_get_areaUnit, _set_areaUnit)

    def as_dict(self):
        d = dict()
        if self.__doesIncludeGainOrLoss is not None:
            d['doesIncludeGainOrLoss'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__doesIncludeGainOrLoss]
        if self.__a1 is not None:
            d['a1'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a1]
        if self.__a2 is not None:
            d['a2'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a2]
        if self.__a3 is not None:
            d['a3'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a3]
        if self.__a4 is not None:
            d['a4'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a4]
        if self.__a5 is not None:
            d['a5'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a5]
        if self.__b1A is not None:
            d['b1A'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b1A]
        if self.__b1B is not None:
            d['b1B'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b1B]
        if self.__b1C is not None:
            d['b1C'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b1C]
        if self.__b2 is not None:
            d['b2'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b2]
        if self.__b8 is not None:
            d['b8'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b8]
        if self.__c1 is not None:
            d['c1'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__c1]
        if self.__c2 is not None:
            d['c2'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__c2]
        if self.__d1 is not None:
            d['d1'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__d1]
        if self.__d2 is not None:
            d['d2'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__d2]
        if self.__other is not None:
            d['other'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__other]
        if self.__totals is not None:
            d['totals'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__totals]
        if self.__areaUnit is not None:
            d['areaUnit'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__areaUnit]
        return d


class DeclarationOfInterest:

    _types_map = {
        'isRelated': {'type': list, 'subtype': None},
        'relationDetails': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, isRelated=None, relationDetails=None
                 ):
        self.__isRelated = isRelated
        self.__relationDetails = relationDetails

    def _get_isRelated(self):
        return self.__isRelated

    def _set_isRelated(self, value):
        if not isinstance(value, list):
            raise TypeError("isRelated must be list")
        self.__isRelated = value
    isRelated = property(_get_isRelated, _set_isRelated)

    def _get_relationDetails(self):
        return self.__relationDetails

    def _set_relationDetails(self, value):
        if not isinstance(value, list):
            raise TypeError("relationDetails must be list")
        self.__relationDetails = value
    relationDetails = property(_get_relationDetails, _set_relationDetails)

    def as_dict(self):
        d = dict()
        if self.__isRelated is not None:
            d['isRelated'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__isRelated]
        if self.__relationDetails is not None:
            d['relationDetails'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__relationDetails]
        return d


class Proposal:

    _types_map = {
        'schemaVersion': {'type': list, 'subtype': None},
        'applicationHeader': {'type': list, 'subtype': None},
        'fileAttachments': {'type': list, 'subtype': None},
        'applicant': {'type': list, 'subtype': None},
        'agent': {'type': list, 'subtype': None},
        'siteLocation': {'type': list, 'subtype': None},
        'applicationScenario': {'type': list, 'subtype': None},
        'consentRegimes': {'type': list, 'subtype': None},
        'applicationData': {'type': list, 'subtype': None},
        'declarationOfInterest': {'type': list, 'subtype': None},
        'declaration': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, schemaVersion=None, applicationHeader=None, fileAttachments=None, applicant=None, agent=None, siteLocation=None, applicationScenario=None, consentRegimes=None, applicationData=None, declarationOfInterest=None, declaration=None
                 ):
        self.__schemaVersion = schemaVersion
        self.__applicationHeader = applicationHeader
        self.__fileAttachments = fileAttachments
        self.__applicant = applicant
        self.__agent = agent
        self.__siteLocation = siteLocation
        self.__applicationScenario = applicationScenario
        self.__consentRegimes = consentRegimes
        self.__applicationData = applicationData
        self.__declarationOfInterest = declarationOfInterest
        self.__declaration = declaration

    def _get_schemaVersion(self):
        return self.__schemaVersion

    def _set_schemaVersion(self, value):
        if not isinstance(value, list):
            raise TypeError("schemaVersion must be list")
        self.__schemaVersion = value
    schemaVersion = property(_get_schemaVersion, _set_schemaVersion)

    def _get_applicationHeader(self):
        return self.__applicationHeader

    def _set_applicationHeader(self, value):
        if not isinstance(value, list):
            raise TypeError("applicationHeader must be list")
        self.__applicationHeader = value
    applicationHeader = property(_get_applicationHeader, _set_applicationHeader)

    def _get_fileAttachments(self):
        return self.__fileAttachments

    def _set_fileAttachments(self, value):
        if not isinstance(value, list):
            raise TypeError("fileAttachments must be list")
        self.__fileAttachments = value
    fileAttachments = property(_get_fileAttachments, _set_fileAttachments)

    def _get_applicant(self):
        return self.__applicant

    def _set_applicant(self, value):
        if not isinstance(value, list):
            raise TypeError("applicant must be list")
        self.__applicant = value
    applicant = property(_get_applicant, _set_applicant)

    def _get_agent(self):
        return self.__agent

    def _set_agent(self, value):
        if not isinstance(value, list):
            raise TypeError("agent must be list")
        self.__agent = value
    agent = property(_get_agent, _set_agent)

    def _get_siteLocation(self):
        return self.__siteLocation

    def _set_siteLocation(self, value):
        if not isinstance(value, list):
            raise TypeError("siteLocation must be list")
        self.__siteLocation = value
    siteLocation = property(_get_siteLocation, _set_siteLocation)

    def _get_applicationScenario(self):
        return self.__applicationScenario

    def _set_applicationScenario(self, value):
        if not isinstance(value, list):
            raise TypeError("applicationScenario must be list")
        self.__applicationScenario = value
    applicationScenario = property(_get_applicationScenario, _set_applicationScenario)

    def _get_consentRegimes(self):
        return self.__consentRegimes

    def _set_consentRegimes(self, value):
        if not isinstance(value, list):
            raise TypeError("consentRegimes must be list")
        self.__consentRegimes = value
    consentRegimes = property(_get_consentRegimes, _set_consentRegimes)

    def _get_applicationData(self):
        return self.__applicationData

    def _set_applicationData(self, value):
        if not isinstance(value, list):
            raise TypeError("applicationData must be list")
        self.__applicationData = value
    applicationData = property(_get_applicationData, _set_applicationData)

    def _get_declarationOfInterest(self):
        return self.__declarationOfInterest

    def _set_declarationOfInterest(self, value):
        if not isinstance(value, list):
            raise TypeError("declarationOfInterest must be list")
        self.__declarationOfInterest = value
    declarationOfInterest = property(_get_declarationOfInterest, _set_declarationOfInterest)

    def _get_declaration(self):
        return self.__declaration

    def _set_declaration(self, value):
        if not isinstance(value, list):
            raise TypeError("declaration must be list")
        self.__declaration = value
    declaration = property(_get_declaration, _set_declaration)

    def as_dict(self):
        d = dict()
        if self.__schemaVersion is not None:
            d['schemaVersion'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__schemaVersion]
        if self.__applicationHeader is not None:
            d['applicationHeader'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__applicationHeader]
        if self.__fileAttachments is not None:
            d['fileAttachments'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__fileAttachments]
        if self.__applicant is not None:
            d['applicant'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__applicant]
        if self.__agent is not None:
            d['agent'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__agent]
        if self.__siteLocation is not None:
            d['siteLocation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__siteLocation]
        if self.__applicationScenario is not None:
            d['applicationScenario'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__applicationScenario]
        if self.__consentRegimes is not None:
            d['consentRegimes'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__consentRegimes]
        if self.__applicationData is not None:
            d['applicationData'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__applicationData]
        if self.__declarationOfInterest is not None:
            d['declarationOfInterest'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__declarationOfInterest]
        if self.__declaration is not None:
            d['declaration'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__declaration]
        return d


class FoulSewage:

    _types_map = {
        'disposal': {'type': list, 'subtype': None},
        'connectExistingDrainage': {'type': list, 'subtype': None},
        'supportingInformation': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, disposal=None, connectExistingDrainage=None, supportingInformation=None
                 ):
        self.__disposal = disposal
        self.__connectExistingDrainage = connectExistingDrainage
        self.__supportingInformation = supportingInformation

    def _get_disposal(self):
        return self.__disposal

    def _set_disposal(self, value):
        if not isinstance(value, list):
            raise TypeError("disposal must be list")
        self.__disposal = value
    disposal = property(_get_disposal, _set_disposal)

    def _get_connectExistingDrainage(self):
        return self.__connectExistingDrainage

    def _set_connectExistingDrainage(self, value):
        if not isinstance(value, list):
            raise TypeError("connectExistingDrainage must be list")
        self.__connectExistingDrainage = value
    connectExistingDrainage = property(_get_connectExistingDrainage, _set_connectExistingDrainage)

    def _get_supportingInformation(self):
        return self.__supportingInformation

    def _set_supportingInformation(self, value):
        if not isinstance(value, list):
            raise TypeError("supportingInformation must be list")
        self.__supportingInformation = value
    supportingInformation = property(_get_supportingInformation, _set_supportingInformation)

    def as_dict(self):
        d = dict()
        if self.__disposal is not None:
            d['disposal'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__disposal]
        if self.__connectExistingDrainage is not None:
            d['connectExistingDrainage'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__connectExistingDrainage]
        if self.__supportingInformation is not None:
            d['supportingInformation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__supportingInformation]
        return d


class Hours:

    _types_map = {
        'a1': {'type': list, 'subtype': None},
        'a2': {'type': list, 'subtype': None},
        'a3': {'type': list, 'subtype': None},
        'a4': {'type': list, 'subtype': None},
        'a5': {'type': list, 'subtype': None},
        'b1A': {'type': list, 'subtype': None},
        'b1B': {'type': list, 'subtype': None},
        'b1C': {'type': list, 'subtype': None},
        'b2': {'type': list, 'subtype': None},
        'b8': {'type': list, 'subtype': None},
        'c1': {'type': list, 'subtype': None},
        'c2': {'type': list, 'subtype': None},
        'c3': {'type': list, 'subtype': None},
        'd1': {'type': list, 'subtype': None},
        'd2': {'type': list, 'subtype': None},
        'other': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, a1=None, a2=None, a3=None, a4=None, a5=None, b1A=None, b1B=None, b1C=None, b2=None, b8=None, c1=None, c2=None, c3=None, d1=None, d2=None, other=None
                 ):
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__a5 = a5
        self.__b1A = b1A
        self.__b1B = b1B
        self.__b1C = b1C
        self.__b2 = b2
        self.__b8 = b8
        self.__c1 = c1
        self.__c2 = c2
        self.__c3 = c3
        self.__d1 = d1
        self.__d2 = d2
        self.__other = other

    def _get_a1(self):
        return self.__a1

    def _set_a1(self, value):
        if not isinstance(value, list):
            raise TypeError("a1 must be list")
        self.__a1 = value
    a1 = property(_get_a1, _set_a1)

    def _get_a2(self):
        return self.__a2

    def _set_a2(self, value):
        if not isinstance(value, list):
            raise TypeError("a2 must be list")
        self.__a2 = value
    a2 = property(_get_a2, _set_a2)

    def _get_a3(self):
        return self.__a3

    def _set_a3(self, value):
        if not isinstance(value, list):
            raise TypeError("a3 must be list")
        self.__a3 = value
    a3 = property(_get_a3, _set_a3)

    def _get_a4(self):
        return self.__a4

    def _set_a4(self, value):
        if not isinstance(value, list):
            raise TypeError("a4 must be list")
        self.__a4 = value
    a4 = property(_get_a4, _set_a4)

    def _get_a5(self):
        return self.__a5

    def _set_a5(self, value):
        if not isinstance(value, list):
            raise TypeError("a5 must be list")
        self.__a5 = value
    a5 = property(_get_a5, _set_a5)

    def _get_b1A(self):
        return self.__b1A

    def _set_b1A(self, value):
        if not isinstance(value, list):
            raise TypeError("b1A must be list")
        self.__b1A = value
    b1A = property(_get_b1A, _set_b1A)

    def _get_b1B(self):
        return self.__b1B

    def _set_b1B(self, value):
        if not isinstance(value, list):
            raise TypeError("b1B must be list")
        self.__b1B = value
    b1B = property(_get_b1B, _set_b1B)

    def _get_b1C(self):
        return self.__b1C

    def _set_b1C(self, value):
        if not isinstance(value, list):
            raise TypeError("b1C must be list")
        self.__b1C = value
    b1C = property(_get_b1C, _set_b1C)

    def _get_b2(self):
        return self.__b2

    def _set_b2(self, value):
        if not isinstance(value, list):
            raise TypeError("b2 must be list")
        self.__b2 = value
    b2 = property(_get_b2, _set_b2)

    def _get_b8(self):
        return self.__b8

    def _set_b8(self, value):
        if not isinstance(value, list):
            raise TypeError("b8 must be list")
        self.__b8 = value
    b8 = property(_get_b8, _set_b8)

    def _get_c1(self):
        return self.__c1

    def _set_c1(self, value):
        if not isinstance(value, list):
            raise TypeError("c1 must be list")
        self.__c1 = value
    c1 = property(_get_c1, _set_c1)

    def _get_c2(self):
        return self.__c2

    def _set_c2(self, value):
        if not isinstance(value, list):
            raise TypeError("c2 must be list")
        self.__c2 = value
    c2 = property(_get_c2, _set_c2)

    def _get_c3(self):
        return self.__c3

    def _set_c3(self, value):
        if not isinstance(value, list):
            raise TypeError("c3 must be list")
        self.__c3 = value
    c3 = property(_get_c3, _set_c3)

    def _get_d1(self):
        return self.__d1

    def _set_d1(self, value):
        if not isinstance(value, list):
            raise TypeError("d1 must be list")
        self.__d1 = value
    d1 = property(_get_d1, _set_d1)

    def _get_d2(self):
        return self.__d2

    def _set_d2(self, value):
        if not isinstance(value, list):
            raise TypeError("d2 must be list")
        self.__d2 = value
    d2 = property(_get_d2, _set_d2)

    def _get_other(self):
        return self.__other

    def _set_other(self, value):
        if not isinstance(value, list):
            raise TypeError("other must be list")
        self.__other = value
    other = property(_get_other, _set_other)

    def as_dict(self):
        d = dict()
        if self.__a1 is not None:
            d['a1'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a1]
        if self.__a2 is not None:
            d['a2'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a2]
        if self.__a3 is not None:
            d['a3'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a3]
        if self.__a4 is not None:
            d['a4'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a4]
        if self.__a5 is not None:
            d['a5'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__a5]
        if self.__b1A is not None:
            d['b1A'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b1A]
        if self.__b1B is not None:
            d['b1B'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b1B]
        if self.__b1C is not None:
            d['b1C'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b1C]
        if self.__b2 is not None:
            d['b2'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b2]
        if self.__b8 is not None:
            d['b8'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__b8]
        if self.__c1 is not None:
            d['c1'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__c1]
        if self.__c2 is not None:
            d['c2'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__c2]
        if self.__c3 is not None:
            d['c3'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__c3]
        if self.__d1 is not None:
            d['d1'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__d1]
        if self.__d2 is not None:
            d['d2'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__d2]
        if self.__other is not None:
            d['other'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__other]
        return d


class VehicleAccess:

    _types_map = {
        'notApplicable': {'type': list, 'subtype': None},
        'dontKnow': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, notApplicable=None, dontKnow=None
                 ):
        self.__notApplicable = notApplicable
        self.__dontKnow = dontKnow

    def _get_notApplicable(self):
        return self.__notApplicable

    def _set_notApplicable(self, value):
        if not isinstance(value, list):
            raise TypeError("notApplicable must be list")
        self.__notApplicable = value
    notApplicable = property(_get_notApplicable, _set_notApplicable)

    def _get_dontKnow(self):
        return self.__dontKnow

    def _set_dontKnow(self, value):
        if not isinstance(value, list):
            raise TypeError("dontKnow must be list")
        self.__dontKnow = value
    dontKnow = property(_get_dontKnow, _set_dontKnow)

    def as_dict(self):
        d = dict()
        if self.__notApplicable is not None:
            d['notApplicable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__notApplicable]
        if self.__dontKnow is not None:
            d['dontKnow'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dontKnow]
        return d


class Sat:

    _types_map = {
        'startTime': {'type': list, 'subtype': None},
        'stopTime': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, startTime=None, stopTime=None
                 ):
        self.__startTime = startTime
        self.__stopTime = stopTime

    def _get_startTime(self):
        return self.__startTime

    def _set_startTime(self, value):
        if not isinstance(value, list):
            raise TypeError("startTime must be list")
        self.__startTime = value
    startTime = property(_get_startTime, _set_startTime)

    def _get_stopTime(self):
        return self.__stopTime

    def _set_stopTime(self, value):
        if not isinstance(value, list):
            raise TypeError("stopTime must be list")
        self.__stopTime = value
    stopTime = property(_get_stopTime, _set_stopTime)

    def as_dict(self):
        d = dict()
        if self.__startTime is not None:
            d['startTime'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__startTime]
        if self.__stopTime is not None:
            d['stopTime'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__stopTime]
        return d


class Advertisement:

    _types_map = {
        'advertDate': {'type': list, 'subtype': None},
        'publicationName': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, advertDate=None, publicationName=None
                 ):
        self.__advertDate = advertDate
        self.__publicationName = publicationName

    def _get_advertDate(self):
        return self.__advertDate

    def _set_advertDate(self, value):
        if not isinstance(value, list):
            raise TypeError("advertDate must be list")
        self.__advertDate = value
    advertDate = property(_get_advertDate, _set_advertDate)

    def _get_publicationName(self):
        return self.__publicationName

    def _set_publicationName(self, value):
        if not isinstance(value, list):
            raise TypeError("publicationName must be list")
        self.__publicationName = value
    publicationName = property(_get_publicationName, _set_publicationName)

    def as_dict(self):
        d = dict()
        if self.__advertDate is not None:
            d['advertDate'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__advertDate]
        if self.__publicationName is not None:
            d['publicationName'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__publicationName]
        return d


class OtherVehicle:

    _types_map = {
        'vehicleTotals': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, vehicleTotals=None
                 ):
        self.__vehicleTotals = vehicleTotals

    def _get_vehicleTotals(self):
        return self.__vehicleTotals

    def _set_vehicleTotals(self, value):
        if not isinstance(value, list):
            raise TypeError("vehicleTotals must be list")
        self.__vehicleTotals = value
    vehicleTotals = property(_get_vehicleTotals, _set_vehicleTotals)

    def as_dict(self):
        d = dict()
        if self.__vehicleTotals is not None:
            d['vehicleTotals'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__vehicleTotals]
        return d


class Payment:

    _types_map = {
        'paymentMethod': {'type': list, 'subtype': None},
        'amountDue': {'type': list, 'subtype': None},
        'amountPaid': {'type': list, 'subtype': None},
        'currency': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, paymentMethod=None, amountDue=None, amountPaid=None, currency=None
                 ):
        self.__paymentMethod = paymentMethod
        self.__amountDue = amountDue
        self.__amountPaid = amountPaid
        self.__currency = currency

    def _get_paymentMethod(self):
        return self.__paymentMethod

    def _set_paymentMethod(self, value):
        if not isinstance(value, list):
            raise TypeError("paymentMethod must be list")
        self.__paymentMethod = value
    paymentMethod = property(_get_paymentMethod, _set_paymentMethod)

    def _get_amountDue(self):
        return self.__amountDue

    def _set_amountDue(self, value):
        if not isinstance(value, list):
            raise TypeError("amountDue must be list")
        self.__amountDue = value
    amountDue = property(_get_amountDue, _set_amountDue)

    def _get_amountPaid(self):
        return self.__amountPaid

    def _set_amountPaid(self, value):
        if not isinstance(value, list):
            raise TypeError("amountPaid must be list")
        self.__amountPaid = value
    amountPaid = property(_get_amountPaid, _set_amountPaid)

    def _get_currency(self):
        return self.__currency

    def _set_currency(self, value):
        if not isinstance(value, list):
            raise TypeError("currency must be list")
        self.__currency = value
    currency = property(_get_currency, _set_currency)

    def as_dict(self):
        d = dict()
        if self.__paymentMethod is not None:
            d['paymentMethod'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__paymentMethod]
        if self.__amountDue is not None:
            d['amountDue'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__amountDue]
        if self.__amountPaid is not None:
            d['amountPaid'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__amountPaid]
        if self.__currency is not None:
            d['currency'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__currency]
        return d


class LastUse:

    _types_map = {
        'lastUseDescription': {'type': list, 'subtype': None},
        'lastUseEndDate': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, lastUseDescription=None, lastUseEndDate=None
                 ):
        self.__lastUseDescription = lastUseDescription
        self.__lastUseEndDate = lastUseEndDate

    def _get_lastUseDescription(self):
        return self.__lastUseDescription

    def _set_lastUseDescription(self, value):
        if not isinstance(value, list):
            raise TypeError("lastUseDescription must be list")
        self.__lastUseDescription = value
    lastUseDescription = property(_get_lastUseDescription, _set_lastUseDescription)

    def _get_lastUseEndDate(self):
        return self.__lastUseEndDate

    def _set_lastUseEndDate(self, value):
        if not isinstance(value, list):
            raise TypeError("lastUseEndDate must be list")
        self.__lastUseEndDate = value
    lastUseEndDate = property(_get_lastUseEndDate, _set_lastUseEndDate)

    def as_dict(self):
        d = dict()
        if self.__lastUseDescription is not None:
            d['lastUseDescription'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__lastUseDescription]
        if self.__lastUseEndDate is not None:
            d['lastUseEndDate'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__lastUseEndDate]
        return d


class Email:

    _types_map = {
        'emailAddress': {'type': list, 'subtype': None},
        'emailPreferred': {'type': list, 'subtype': None},
        'emailUsage': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, emailAddress=None, emailPreferred=None, emailUsage=None
                 ):
        self.__emailAddress = emailAddress
        self.__emailPreferred = emailPreferred
        self.__emailUsage = emailUsage

    def _get_emailAddress(self):
        return self.__emailAddress

    def _set_emailAddress(self, value):
        if not isinstance(value, list):
            raise TypeError("emailAddress must be list")
        self.__emailAddress = value
    emailAddress = property(_get_emailAddress, _set_emailAddress)

    def _get_emailPreferred(self):
        return self.__emailPreferred

    def _set_emailPreferred(self, value):
        if not isinstance(value, list):
            raise TypeError("emailPreferred must be list")
        self.__emailPreferred = value
    emailPreferred = property(_get_emailPreferred, _set_emailPreferred)

    def _get_emailUsage(self):
        return self.__emailUsage

    def _set_emailUsage(self, value):
        if not isinstance(value, list):
            raise TypeError("emailUsage must be list")
        self.__emailUsage = value
    emailUsage = property(_get_emailUsage, _set_emailUsage)

    def as_dict(self):
        d = dict()
        if self.__emailAddress is not None:
            d['emailAddress'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__emailAddress]
        if self.__emailPreferred is not None:
            d['emailPreferred'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__emailPreferred]
        if self.__emailUsage is not None:
            d['emailUsage'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__emailUsage]
        return d


class SupportingInformation:

    _types_map = {
        'additionalInformation': {'type': list, 'subtype': None},
        'reference': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, additionalInformation=None, reference=None
                 ):
        self.__additionalInformation = additionalInformation
        self.__reference = reference

    def _get_additionalInformation(self):
        return self.__additionalInformation

    def _set_additionalInformation(self, value):
        if not isinstance(value, list):
            raise TypeError("additionalInformation must be list")
        self.__additionalInformation = value
    additionalInformation = property(_get_additionalInformation, _set_additionalInformation)

    def _get_reference(self):
        return self.__reference

    def _set_reference(self, value):
        if not isinstance(value, list):
            raise TypeError("reference must be list")
        self.__reference = value
    reference = property(_get_reference, _set_reference)

    def as_dict(self):
        d = dict()
        if self.__additionalInformation is not None:
            d['additionalInformation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__additionalInformation]
        if self.__reference is not None:
            d['reference'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__reference]
        return d


class CommonNo:

    _types_map = {
        'no': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, no=None
                 ):
        self.__no = no

    def _get_no(self):
        return self.__no

    def _set_no(self, value):
        if not isinstance(value, list):
            raise TypeError("no must be list")
        self.__no = value
    no = property(_get_no, _set_no)

    def as_dict(self):
        d = dict()
        if self.__no is not None:
            d['no'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__no]
        return d


class SiteLocation:

    _types_map = {
        'bs7666Address': {'type': list, 'subtype': None},
        'siteGridRefence': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, bs7666Address=None, siteGridRefence=None
                 ):
        self.__bs7666Address = bs7666Address
        self.__siteGridRefence = siteGridRefence

    def _get_bs7666Address(self):
        return self.__bs7666Address

    def _set_bs7666Address(self, value):
        if not isinstance(value, list):
            raise TypeError("bs7666Address must be list")
        self.__bs7666Address = value
    bs7666Address = property(_get_bs7666Address, _set_bs7666Address)

    def _get_siteGridRefence(self):
        return self.__siteGridRefence

    def _set_siteGridRefence(self, value):
        if not isinstance(value, list):
            raise TypeError("siteGridRefence must be list")
        self.__siteGridRefence = value
    siteGridRefence = property(_get_siteGridRefence, _set_siteGridRefence)

    def as_dict(self):
        d = dict()
        if self.__bs7666Address is not None:
            d['bs7666Address'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__bs7666Address]
        if self.__siteGridRefence is not None:
            d['siteGridRefence'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__siteGridRefence]
        return d


class VisitContactDetails:

    _types_map = {
        'contactOther': {'type': list, 'subtype': None},
        'contactAgent': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, contactOther=None, contactAgent=None
                 ):
        self.__contactOther = contactOther
        self.__contactAgent = contactAgent

    def _get_contactOther(self):
        return self.__contactOther

    def _set_contactOther(self, value):
        if not isinstance(value, list):
            raise TypeError("contactOther must be list")
        self.__contactOther = value
    contactOther = property(_get_contactOther, _set_contactOther)

    def _get_contactAgent(self):
        return self.__contactAgent

    def _set_contactAgent(self, value):
        if not isinstance(value, list):
            raise TypeError("contactAgent must be list")
        self.__contactAgent = value
    contactAgent = property(_get_contactAgent, _set_contactAgent)

    def as_dict(self):
        d = dict()
        if self.__contactOther is not None:
            d['contactOther'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__contactOther]
        if self.__contactAgent is not None:
            d['contactAgent'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__contactAgent]
        return d


class B1C:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class WasteManagementDetails:

    _types_map = {
        'inertLandfill': {'type': list, 'subtype': None},
        'nonHazardousLandfill': {'type': list, 'subtype': None},
        'hazardousLandfill': {'type': list, 'subtype': None},
        'wasteIncinerationEnergy': {'type': list, 'subtype': None},
        'otherIncineration': {'type': list, 'subtype': None},
        'landfillGasGenerationPlant': {'type': list, 'subtype': None},
        'pyrolysisGasification': {'type': list, 'subtype': None},
        'metalRecyclingSite': {'type': list, 'subtype': None},
        'transferStations': {'type': list, 'subtype': None},
        'materialRecoveryFacilities': {'type': list, 'subtype': None},
        'householdCivicAmenitySites': {'type': list, 'subtype': None},
        'openWindrowComposting': {'type': list, 'subtype': None},
        'invesselComposting': {'type': list, 'subtype': None},
        'anaerobicDigestion': {'type': list, 'subtype': None},
        'mbtTreatment': {'type': list, 'subtype': None},
        'sewageTreatmentWorks': {'type': list, 'subtype': None},
        'otherTreatment': {'type': list, 'subtype': None},
        'recyclingFacilitiesCDEWaste': {'type': list, 'subtype': None},
        'storageOfWaste': {'type': list, 'subtype': None},
        'otherWasteManagement': {'type': list, 'subtype': None},
        'otherDevelopments': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, inertLandfill=None, nonHazardousLandfill=None, hazardousLandfill=None, wasteIncinerationEnergy=None, otherIncineration=None, landfillGasGenerationPlant=None, pyrolysisGasification=None, metalRecyclingSite=None, transferStations=None, materialRecoveryFacilities=None, householdCivicAmenitySites=None, openWindrowComposting=None, invesselComposting=None, anaerobicDigestion=None, mbtTreatment=None, sewageTreatmentWorks=None, otherTreatment=None, recyclingFacilitiesCDEWaste=None, storageOfWaste=None, otherWasteManagement=None, otherDevelopments=None
                 ):
        self.__inertLandfill = inertLandfill
        self.__nonHazardousLandfill = nonHazardousLandfill
        self.__hazardousLandfill = hazardousLandfill
        self.__wasteIncinerationEnergy = wasteIncinerationEnergy
        self.__otherIncineration = otherIncineration
        self.__landfillGasGenerationPlant = landfillGasGenerationPlant
        self.__pyrolysisGasification = pyrolysisGasification
        self.__metalRecyclingSite = metalRecyclingSite
        self.__transferStations = transferStations
        self.__materialRecoveryFacilities = materialRecoveryFacilities
        self.__householdCivicAmenitySites = householdCivicAmenitySites
        self.__openWindrowComposting = openWindrowComposting
        self.__invesselComposting = invesselComposting
        self.__anaerobicDigestion = anaerobicDigestion
        self.__mbtTreatment = mbtTreatment
        self.__sewageTreatmentWorks = sewageTreatmentWorks
        self.__otherTreatment = otherTreatment
        self.__recyclingFacilitiesCDEWaste = recyclingFacilitiesCDEWaste
        self.__storageOfWaste = storageOfWaste
        self.__otherWasteManagement = otherWasteManagement
        self.__otherDevelopments = otherDevelopments

    def _get_inertLandfill(self):
        return self.__inertLandfill

    def _set_inertLandfill(self, value):
        if not isinstance(value, list):
            raise TypeError("inertLandfill must be list")
        self.__inertLandfill = value
    inertLandfill = property(_get_inertLandfill, _set_inertLandfill)

    def _get_nonHazardousLandfill(self):
        return self.__nonHazardousLandfill

    def _set_nonHazardousLandfill(self, value):
        if not isinstance(value, list):
            raise TypeError("nonHazardousLandfill must be list")
        self.__nonHazardousLandfill = value
    nonHazardousLandfill = property(_get_nonHazardousLandfill, _set_nonHazardousLandfill)

    def _get_hazardousLandfill(self):
        return self.__hazardousLandfill

    def _set_hazardousLandfill(self, value):
        if not isinstance(value, list):
            raise TypeError("hazardousLandfill must be list")
        self.__hazardousLandfill = value
    hazardousLandfill = property(_get_hazardousLandfill, _set_hazardousLandfill)

    def _get_wasteIncinerationEnergy(self):
        return self.__wasteIncinerationEnergy

    def _set_wasteIncinerationEnergy(self, value):
        if not isinstance(value, list):
            raise TypeError("wasteIncinerationEnergy must be list")
        self.__wasteIncinerationEnergy = value
    wasteIncinerationEnergy = property(_get_wasteIncinerationEnergy, _set_wasteIncinerationEnergy)

    def _get_otherIncineration(self):
        return self.__otherIncineration

    def _set_otherIncineration(self, value):
        if not isinstance(value, list):
            raise TypeError("otherIncineration must be list")
        self.__otherIncineration = value
    otherIncineration = property(_get_otherIncineration, _set_otherIncineration)

    def _get_landfillGasGenerationPlant(self):
        return self.__landfillGasGenerationPlant

    def _set_landfillGasGenerationPlant(self, value):
        if not isinstance(value, list):
            raise TypeError("landfillGasGenerationPlant must be list")
        self.__landfillGasGenerationPlant = value
    landfillGasGenerationPlant = property(
        _get_landfillGasGenerationPlant, _set_landfillGasGenerationPlant)

    def _get_pyrolysisGasification(self):
        return self.__pyrolysisGasification

    def _set_pyrolysisGasification(self, value):
        if not isinstance(value, list):
            raise TypeError("pyrolysisGasification must be list")
        self.__pyrolysisGasification = value
    pyrolysisGasification = property(_get_pyrolysisGasification, _set_pyrolysisGasification)

    def _get_metalRecyclingSite(self):
        return self.__metalRecyclingSite

    def _set_metalRecyclingSite(self, value):
        if not isinstance(value, list):
            raise TypeError("metalRecyclingSite must be list")
        self.__metalRecyclingSite = value
    metalRecyclingSite = property(_get_metalRecyclingSite, _set_metalRecyclingSite)

    def _get_transferStations(self):
        return self.__transferStations

    def _set_transferStations(self, value):
        if not isinstance(value, list):
            raise TypeError("transferStations must be list")
        self.__transferStations = value
    transferStations = property(_get_transferStations, _set_transferStations)

    def _get_materialRecoveryFacilities(self):
        return self.__materialRecoveryFacilities

    def _set_materialRecoveryFacilities(self, value):
        if not isinstance(value, list):
            raise TypeError("materialRecoveryFacilities must be list")
        self.__materialRecoveryFacilities = value
    materialRecoveryFacilities = property(
        _get_materialRecoveryFacilities, _set_materialRecoveryFacilities)

    def _get_householdCivicAmenitySites(self):
        return self.__householdCivicAmenitySites

    def _set_householdCivicAmenitySites(self, value):
        if not isinstance(value, list):
            raise TypeError("householdCivicAmenitySites must be list")
        self.__householdCivicAmenitySites = value
    householdCivicAmenitySites = property(
        _get_householdCivicAmenitySites, _set_householdCivicAmenitySites)

    def _get_openWindrowComposting(self):
        return self.__openWindrowComposting

    def _set_openWindrowComposting(self, value):
        if not isinstance(value, list):
            raise TypeError("openWindrowComposting must be list")
        self.__openWindrowComposting = value
    openWindrowComposting = property(_get_openWindrowComposting, _set_openWindrowComposting)

    def _get_invesselComposting(self):
        return self.__invesselComposting

    def _set_invesselComposting(self, value):
        if not isinstance(value, list):
            raise TypeError("invesselComposting must be list")
        self.__invesselComposting = value
    invesselComposting = property(_get_invesselComposting, _set_invesselComposting)

    def _get_anaerobicDigestion(self):
        return self.__anaerobicDigestion

    def _set_anaerobicDigestion(self, value):
        if not isinstance(value, list):
            raise TypeError("anaerobicDigestion must be list")
        self.__anaerobicDigestion = value
    anaerobicDigestion = property(_get_anaerobicDigestion, _set_anaerobicDigestion)

    def _get_mbtTreatment(self):
        return self.__mbtTreatment

    def _set_mbtTreatment(self, value):
        if not isinstance(value, list):
            raise TypeError("mbtTreatment must be list")
        self.__mbtTreatment = value
    mbtTreatment = property(_get_mbtTreatment, _set_mbtTreatment)

    def _get_sewageTreatmentWorks(self):
        return self.__sewageTreatmentWorks

    def _set_sewageTreatmentWorks(self, value):
        if not isinstance(value, list):
            raise TypeError("sewageTreatmentWorks must be list")
        self.__sewageTreatmentWorks = value
    sewageTreatmentWorks = property(_get_sewageTreatmentWorks, _set_sewageTreatmentWorks)

    def _get_otherTreatment(self):
        return self.__otherTreatment

    def _set_otherTreatment(self, value):
        if not isinstance(value, list):
            raise TypeError("otherTreatment must be list")
        self.__otherTreatment = value
    otherTreatment = property(_get_otherTreatment, _set_otherTreatment)

    def _get_recyclingFacilitiesCDEWaste(self):
        return self.__recyclingFacilitiesCDEWaste

    def _set_recyclingFacilitiesCDEWaste(self, value):
        if not isinstance(value, list):
            raise TypeError("recyclingFacilitiesCDEWaste must be list")
        self.__recyclingFacilitiesCDEWaste = value
    recyclingFacilitiesCDEWaste = property(
        _get_recyclingFacilitiesCDEWaste, _set_recyclingFacilitiesCDEWaste)

    def _get_storageOfWaste(self):
        return self.__storageOfWaste

    def _set_storageOfWaste(self, value):
        if not isinstance(value, list):
            raise TypeError("storageOfWaste must be list")
        self.__storageOfWaste = value
    storageOfWaste = property(_get_storageOfWaste, _set_storageOfWaste)

    def _get_otherWasteManagement(self):
        return self.__otherWasteManagement

    def _set_otherWasteManagement(self, value):
        if not isinstance(value, list):
            raise TypeError("otherWasteManagement must be list")
        self.__otherWasteManagement = value
    otherWasteManagement = property(_get_otherWasteManagement, _set_otherWasteManagement)

    def _get_otherDevelopments(self):
        return self.__otherDevelopments

    def _set_otherDevelopments(self, value):
        if not isinstance(value, list):
            raise TypeError("otherDevelopments must be list")
        self.__otherDevelopments = value
    otherDevelopments = property(_get_otherDevelopments, _set_otherDevelopments)

    def as_dict(self):
        d = dict()
        if self.__inertLandfill is not None:
            d['inertLandfill'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__inertLandfill]
        if self.__nonHazardousLandfill is not None:
            d['nonHazardousLandfill'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__nonHazardousLandfill]
        if self.__hazardousLandfill is not None:
            d['hazardousLandfill'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__hazardousLandfill]
        if self.__wasteIncinerationEnergy is not None:
            d['wasteIncinerationEnergy'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__wasteIncinerationEnergy]
        if self.__otherIncineration is not None:
            d['otherIncineration'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__otherIncineration]
        if self.__landfillGasGenerationPlant is not None:
            d['landfillGasGenerationPlant'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__landfillGasGenerationPlant]
        if self.__pyrolysisGasification is not None:
            d['pyrolysisGasification'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__pyrolysisGasification]
        if self.__metalRecyclingSite is not None:
            d['metalRecyclingSite'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__metalRecyclingSite]
        if self.__transferStations is not None:
            d['transferStations'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__transferStations]
        if self.__materialRecoveryFacilities is not None:
            d['materialRecoveryFacilities'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__materialRecoveryFacilities]
        if self.__householdCivicAmenitySites is not None:
            d['householdCivicAmenitySites'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__householdCivicAmenitySites]
        if self.__openWindrowComposting is not None:
            d['openWindrowComposting'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__openWindrowComposting]
        if self.__invesselComposting is not None:
            d['invesselComposting'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__invesselComposting]
        if self.__anaerobicDigestion is not None:
            d['anaerobicDigestion'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__anaerobicDigestion]
        if self.__mbtTreatment is not None:
            d['mbtTreatment'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__mbtTreatment]
        if self.__sewageTreatmentWorks is not None:
            d['sewageTreatmentWorks'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__sewageTreatmentWorks]
        if self.__otherTreatment is not None:
            d['otherTreatment'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__otherTreatment]
        if self.__recyclingFacilitiesCDEWaste is not None:
            d['recyclingFacilitiesCDEWaste'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__recyclingFacilitiesCDEWaste]
        if self.__storageOfWaste is not None:
            d['storageOfWaste'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__storageOfWaste]
        if self.__otherWasteManagement is not None:
            d['otherWasteManagement'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__otherWasteManagement]
        if self.__otherDevelopments is not None:
            d['otherDevelopments'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__otherDevelopments]
        return d


class SocialRented:

    _types_map = {
        'total': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, total=None
                 ):
        self.__total = total

    def _get_total(self):
        return self.__total

    def _set_total(self, value):
        if not isinstance(value, list):
            raise TypeError("total must be list")
        self.__total = value
    total = property(_get_total, _set_total)

    def as_dict(self):
        d = dict()
        if self.__total is not None:
            d['total'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__total]
        return d


class NonHazardousLandfill:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class Declaration:

    _types_map = {
        'declarationDate': {'type': list, 'subtype': None},
        'declarationMade': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, declarationDate=None, declarationMade=None
                 ):
        self.__declarationDate = declarationDate
        self.__declarationMade = declarationMade

    def _get_declarationDate(self):
        return self.__declarationDate

    def _set_declarationDate(self, value):
        if not isinstance(value, list):
            raise TypeError("declarationDate must be list")
        self.__declarationDate = value
    declarationDate = property(_get_declarationDate, _set_declarationDate)

    def _get_declarationMade(self):
        return self.__declarationMade

    def _set_declarationMade(self, value):
        if not isinstance(value, list):
            raise TypeError("declarationMade must be list")
        self.__declarationMade = value
    declarationMade = property(_get_declarationMade, _set_declarationMade)

    def as_dict(self):
        d = dict()
        if self.__declarationDate is not None:
            d['declarationDate'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__declarationDate]
        if self.__declarationMade is not None:
            d['declarationMade'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__declarationMade]
        return d


class PaperSize:

    _types_map = {
        'standardSize': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, standardSize=None
                 ):
        self.__standardSize = standardSize

    def _get_standardSize(self):
        return self.__standardSize

    def _set_standardSize(self, value):
        if not isinstance(value, list):
            raise TypeError("standardSize must be list")
        self.__standardSize = value
    standardSize = property(_get_standardSize, _set_standardSize)

    def as_dict(self):
        d = dict()
        if self.__standardSize is not None:
            d['standardSize'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__standardSize]
        return d


class Hazardous:

    _types_map = {
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, maxAnnualOperationalThroughput=None
                 ):
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class ExternalWalls:

    _types_map = {
        'notApplicable': {'type': list, 'subtype': None},
        'dontKnow': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, notApplicable=None, dontKnow=None
                 ):
        self.__notApplicable = notApplicable
        self.__dontKnow = dontKnow

    def _get_notApplicable(self):
        return self.__notApplicable

    def _set_notApplicable(self, value):
        if not isinstance(value, list):
            raise TypeError("notApplicable must be list")
        self.__notApplicable = value
    notApplicable = property(_get_notApplicable, _set_notApplicable)

    def _get_dontKnow(self):
        return self.__dontKnow

    def _set_dontKnow(self, value):
        if not isinstance(value, list):
            raise TypeError("dontKnow must be list")
        self.__dontKnow = value
    dontKnow = property(_get_dontKnow, _set_dontKnow)

    def as_dict(self):
        d = dict()
        if self.__notApplicable is not None:
            d['notApplicable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__notApplicable]
        if self.__dontKnow is not None:
            d['dontKnow'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dontKnow]
        return d


class Disability:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        '_new': {'type': list, 'subtype': None},
        'difference': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, _new=None, difference=None
                 ):
        self.__existing = existing
        self.___new = _new
        self.__difference = difference

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get__new(self):
        return self.___new

    def _set__new(self, value):
        if not isinstance(value, list):
            raise TypeError("_new must be list")
        self.___new = value
    _new = property(_get__new, _set__new)

    def _get_difference(self):
        return self.__difference

    def _set_difference(self, value):
        if not isinstance(value, list):
            raise TypeError("difference must be list")
        self.__difference = value
    difference = property(_get_difference, _set_difference)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.___new is not None:
            d['_new'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.___new]
        if self.__difference is not None:
            d['difference'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__difference]
        return d


class StopTime:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class MaxAnnualOperationalThroughput:

    _types_map = {
        'volumeUnit': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, volumeUnit=None
                 ):
        self.__volumeUnit = volumeUnit

    def _get_volumeUnit(self):
        return self.__volumeUnit

    def _set_volumeUnit(self, value):
        if not isinstance(value, list):
            raise TypeError("volumeUnit must be list")
        self.__volumeUnit = value
    volumeUnit = property(_get_volumeUnit, _set_volumeUnit)

    def as_dict(self):
        d = dict()
        if self.__volumeUnit is not None:
            d['volumeUnit'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__volumeUnit]
        return d


class ExternalDoors:

    _types_map = {
        'notApplicable': {'type': list, 'subtype': None},
        'dontKnow': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, notApplicable=None, dontKnow=None
                 ):
        self.__notApplicable = notApplicable
        self.__dontKnow = dontKnow

    def _get_notApplicable(self):
        return self.__notApplicable

    def _set_notApplicable(self, value):
        if not isinstance(value, list):
            raise TypeError("notApplicable must be list")
        self.__notApplicable = value
    notApplicable = property(_get_notApplicable, _set_notApplicable)

    def _get_dontKnow(self):
        return self.__dontKnow

    def _set_dontKnow(self, value):
        if not isinstance(value, list):
            raise TypeError("dontKnow must be list")
        self.__dontKnow = value
    dontKnow = property(_get_dontKnow, _set_dontKnow)

    def as_dict(self):
        d = dict()
        if self.__notApplicable is not None:
            d['notApplicable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__notApplicable]
        if self.__dontKnow is not None:
            d['dontKnow'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dontKnow]
        return d


class EndRange:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class C2:

    _types_map = {
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
        'roomInformation': {'type': list, 'subtype': None},
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None, roomInformation=None, monToFri=None, sat=None, sunBH=None
                 ):
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace
        self.__roomInformation = roomInformation
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def _get_roomInformation(self):
        return self.__roomInformation

    def _set_roomInformation(self, value):
        if not isinstance(value, list):
            raise TypeError("roomInformation must be list")
        self.__roomInformation = value
    roomInformation = property(_get_roomInformation, _set_roomInformation)

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def as_dict(self):
        d = dict()
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        if self.__roomInformation is not None:
            d['roomInformation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__roomInformation]
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        return d


class Motorcycle:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        '_new': {'type': list, 'subtype': None},
        'difference': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, _new=None, difference=None
                 ):
        self.__existing = existing
        self.___new = _new
        self.__difference = difference

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get__new(self):
        return self.___new

    def _set__new(self, value):
        if not isinstance(value, list):
            raise TypeError("_new must be list")
        self.___new = value
    _new = property(_get__new, _set__new)

    def _get_difference(self):
        return self.__difference

    def _set_difference(self, value):
        if not isinstance(value, list):
            raise TypeError("difference must be list")
        self.__difference = value
    difference = property(_get_difference, _set_difference)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.___new is not None:
            d['_new'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.___new]
        if self.__difference is not None:
            d['difference'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__difference]
        return d


class SewageTreatmentWorks:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class SiteArea:

    _types_map = {
        'value': {'type': list, 'subtype': None},
        'areaUnit': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, value=None, areaUnit=None
                 ):
        self.__value = value
        self.__areaUnit = areaUnit

    def _get_value(self):
        return self.__value

    def _set_value(self, value):
        if not isinstance(value, list):
            raise TypeError("value must be list")
        self.__value = value
    value = property(_get_value, _set_value)

    def _get_areaUnit(self):
        return self.__areaUnit

    def _set_areaUnit(self, value):
        if not isinstance(value, list):
            raise TypeError("areaUnit must be list")
        self.__areaUnit = value
    areaUnit = property(_get_areaUnit, _set_areaUnit)

    def as_dict(self):
        d = dict()
        if self.__value is not None:
            d['value'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__value]
        if self.__areaUnit is not None:
            d['areaUnit'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__areaUnit]
        return d


class KeyWorker:

    _types_map = {
        'total': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, total=None
                 ):
        self.__total = total

    def _get_total(self):
        return self.__total

    def _set_total(self, value):
        if not isinstance(value, list):
            raise TypeError("total must be list")
        self.__total = value
    total = property(_get_total, _set_total)

    def as_dict(self):
        d = dict()
        if self.__total is not None:
            d['total'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__total]
        return d


class Disposal:

    _types_map = {
        'mainsSewer': {'type': list, 'subtype': None},
        'specifiedOther': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, mainsSewer=None, specifiedOther=None
                 ):
        self.__mainsSewer = mainsSewer
        self.__specifiedOther = specifiedOther

    def _get_mainsSewer(self):
        return self.__mainsSewer

    def _set_mainsSewer(self, value):
        if not isinstance(value, list):
            raise TypeError("mainsSewer must be list")
        self.__mainsSewer = value
    mainsSewer = property(_get_mainsSewer, _set_mainsSewer)

    def _get_specifiedOther(self):
        return self.__specifiedOther

    def _set_specifiedOther(self, value):
        if not isinstance(value, list):
            raise TypeError("specifiedOther must be list")
        self.__specifiedOther = value
    specifiedOther = property(_get_specifiedOther, _set_specifiedOther)

    def as_dict(self):
        d = dict()
        if self.__mainsSewer is not None:
            d['mainsSewer'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__mainsSewer]
        if self.__specifiedOther is not None:
            d['specifiedOther'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__specifiedOther]
        return d


class FullTreesHedges:

    _types_map = {
        'treesHedgesOnSite': {'type': list, 'subtype': None},
        'treesHedgesAdjacent': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, treesHedgesOnSite=None, treesHedgesAdjacent=None
                 ):
        self.__treesHedgesOnSite = treesHedgesOnSite
        self.__treesHedgesAdjacent = treesHedgesAdjacent

    def _get_treesHedgesOnSite(self):
        return self.__treesHedgesOnSite

    def _set_treesHedgesOnSite(self, value):
        if not isinstance(value, list):
            raise TypeError("treesHedgesOnSite must be list")
        self.__treesHedgesOnSite = value
    treesHedgesOnSite = property(_get_treesHedgesOnSite, _set_treesHedgesOnSite)

    def _get_treesHedgesAdjacent(self):
        return self.__treesHedgesAdjacent

    def _set_treesHedgesAdjacent(self, value):
        if not isinstance(value, list):
            raise TypeError("treesHedgesAdjacent must be list")
        self.__treesHedgesAdjacent = value
    treesHedgesAdjacent = property(_get_treesHedgesAdjacent, _set_treesHedgesAdjacent)

    def as_dict(self):
        d = dict()
        if self.__treesHedgesOnSite is not None:
            d['treesHedgesOnSite'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__treesHedgesOnSite]
        if self.__treesHedgesAdjacent is not None:
            d['treesHedgesAdjacent'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__treesHedgesAdjacent]
        return d


class PrintInformation:

    _types_map = {
        'paperSize': {'type': list, 'subtype': None},
        'hasBeenPrinted': {'type': list, 'subtype': None},
        'hasScale': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, paperSize=None, hasBeenPrinted=None, hasScale=None
                 ):
        self.__paperSize = paperSize
        self.__hasBeenPrinted = hasBeenPrinted
        self.__hasScale = hasScale

    def _get_paperSize(self):
        return self.__paperSize

    def _set_paperSize(self, value):
        if not isinstance(value, list):
            raise TypeError("paperSize must be list")
        self.__paperSize = value
    paperSize = property(_get_paperSize, _set_paperSize)

    def _get_hasBeenPrinted(self):
        return self.__hasBeenPrinted

    def _set_hasBeenPrinted(self, value):
        if not isinstance(value, list):
            raise TypeError("hasBeenPrinted must be list")
        self.__hasBeenPrinted = value
    hasBeenPrinted = property(_get_hasBeenPrinted, _set_hasBeenPrinted)

    def _get_hasScale(self):
        return self.__hasScale

    def _set_hasScale(self, value):
        if not isinstance(value, list):
            raise TypeError("hasScale must be list")
        self.__hasScale = value
    hasScale = property(_get_hasScale, _set_hasScale)

    def as_dict(self):
        d = dict()
        if self.__paperSize is not None:
            d['paperSize'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__paperSize]
        if self.__hasBeenPrinted is not None:
            d['hasBeenPrinted'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__hasBeenPrinted]
        if self.__hasScale is not None:
            d['hasScale'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__hasScale]
        return d


class FloodRisk:

    _types_map = {
        'siteInFloodRiskArea': {'type': list, 'subtype': None},
        'floodRiskTable': {'type': list, 'subtype': None},
        'proposalNearWatercourse': {'type': list, 'subtype': None},
        'proposalIncreaseFloodrisk': {'type': list, 'subtype': None},
        'surfaceWaterDischarge': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, siteInFloodRiskArea=None, floodRiskTable=None, proposalNearWatercourse=None, proposalIncreaseFloodrisk=None, surfaceWaterDischarge=None
                 ):
        self.__siteInFloodRiskArea = siteInFloodRiskArea
        self.__floodRiskTable = floodRiskTable
        self.__proposalNearWatercourse = proposalNearWatercourse
        self.__proposalIncreaseFloodrisk = proposalIncreaseFloodrisk
        self.__surfaceWaterDischarge = surfaceWaterDischarge

    def _get_siteInFloodRiskArea(self):
        return self.__siteInFloodRiskArea

    def _set_siteInFloodRiskArea(self, value):
        if not isinstance(value, list):
            raise TypeError("siteInFloodRiskArea must be list")
        self.__siteInFloodRiskArea = value
    siteInFloodRiskArea = property(_get_siteInFloodRiskArea, _set_siteInFloodRiskArea)

    def _get_floodRiskTable(self):
        return self.__floodRiskTable

    def _set_floodRiskTable(self, value):
        if not isinstance(value, list):
            raise TypeError("floodRiskTable must be list")
        self.__floodRiskTable = value
    floodRiskTable = property(_get_floodRiskTable, _set_floodRiskTable)

    def _get_proposalNearWatercourse(self):
        return self.__proposalNearWatercourse

    def _set_proposalNearWatercourse(self, value):
        if not isinstance(value, list):
            raise TypeError("proposalNearWatercourse must be list")
        self.__proposalNearWatercourse = value
    proposalNearWatercourse = property(_get_proposalNearWatercourse, _set_proposalNearWatercourse)

    def _get_proposalIncreaseFloodrisk(self):
        return self.__proposalIncreaseFloodrisk

    def _set_proposalIncreaseFloodrisk(self, value):
        if not isinstance(value, list):
            raise TypeError("proposalIncreaseFloodrisk must be list")
        self.__proposalIncreaseFloodrisk = value
    proposalIncreaseFloodrisk = property(
        _get_proposalIncreaseFloodrisk, _set_proposalIncreaseFloodrisk)

    def _get_surfaceWaterDischarge(self):
        return self.__surfaceWaterDischarge

    def _set_surfaceWaterDischarge(self, value):
        if not isinstance(value, list):
            raise TypeError("surfaceWaterDischarge must be list")
        self.__surfaceWaterDischarge = value
    surfaceWaterDischarge = property(_get_surfaceWaterDischarge, _set_surfaceWaterDischarge)

    def as_dict(self):
        d = dict()
        if self.__siteInFloodRiskArea is not None:
            d['siteInFloodRiskArea'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__siteInFloodRiskArea]
        if self.__floodRiskTable is not None:
            d['floodRiskTable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__floodRiskTable]
        if self.__proposalNearWatercourse is not None:
            d['proposalNearWatercourse'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__proposalNearWatercourse]
        if self.__proposalIncreaseFloodrisk is not None:
            d['proposalIncreaseFloodrisk'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__proposalIncreaseFloodrisk]
        if self.__surfaceWaterDischarge is not None:
            d['surfaceWaterDischarge'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__surfaceWaterDischarge]
        return d


class No:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class Signatory:

    _types_map = {
        'personNameTitle': {'type': list, 'subtype': None},
        'personGivenName': {'type': list, 'subtype': None},
        'personFamilyName': {'type': list, 'subtype': None},
        'personRole': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, personNameTitle=None, personGivenName=None, personFamilyName=None, personRole=None
                 ):
        self.__personNameTitle = personNameTitle
        self.__personGivenName = personGivenName
        self.__personFamilyName = personFamilyName
        self.__personRole = personRole

    def _get_personNameTitle(self):
        return self.__personNameTitle

    def _set_personNameTitle(self, value):
        if not isinstance(value, list):
            raise TypeError("personNameTitle must be list")
        self.__personNameTitle = value
    personNameTitle = property(_get_personNameTitle, _set_personNameTitle)

    def _get_personGivenName(self):
        return self.__personGivenName

    def _set_personGivenName(self, value):
        if not isinstance(value, list):
            raise TypeError("personGivenName must be list")
        self.__personGivenName = value
    personGivenName = property(_get_personGivenName, _set_personGivenName)

    def _get_personFamilyName(self):
        return self.__personFamilyName

    def _set_personFamilyName(self, value):
        if not isinstance(value, list):
            raise TypeError("personFamilyName must be list")
        self.__personFamilyName = value
    personFamilyName = property(_get_personFamilyName, _set_personFamilyName)

    def _get_personRole(self):
        return self.__personRole

    def _set_personRole(self, value):
        if not isinstance(value, list):
            raise TypeError("personRole must be list")
        self.__personRole = value
    personRole = property(_get_personRole, _set_personRole)

    def as_dict(self):
        d = dict()
        if self.__personNameTitle is not None:
            d['personNameTitle'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__personNameTitle]
        if self.__personGivenName is not None:
            d['personGivenName'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__personGivenName]
        if self.__personFamilyName is not None:
            d['personFamilyName'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__personFamilyName]
        if self.__personRole is not None:
            d['personRole'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__personRole]
        return d


class Parking:

    _types_map = {
        'fullParking': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, fullParking=None
                 ):
        self.__fullParking = fullParking

    def _get_fullParking(self):
        return self.__fullParking

    def _set_fullParking(self, value):
        if not isinstance(value, list):
            raise TypeError("fullParking must be list")
        self.__fullParking = value
    fullParking = property(_get_fullParking, _set_fullParking)

    def as_dict(self):
        d = dict()
        if self.__fullParking is not None:
            d['fullParking'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__fullParking]
        return d


class NoticeGiven:

    _types_map = {
        'noticeGivenTo': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, noticeGivenTo=None
                 ):
        self.__noticeGivenTo = noticeGivenTo

    def _get_noticeGivenTo(self):
        return self.__noticeGivenTo

    def _set_noticeGivenTo(self, value):
        if not isinstance(value, list):
            raise TypeError("noticeGivenTo must be list")
        self.__noticeGivenTo = value
    noticeGivenTo = property(_get_noticeGivenTo, _set_noticeGivenTo)

    def as_dict(self):
        d = dict()
        if self.__noticeGivenTo is not None:
            d['noticeGivenTo'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__noticeGivenTo]
        return d


class FloodRiskTable:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class Roof:

    _types_map = {
        'notApplicable': {'type': list, 'subtype': None},
        'dontKnow': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, notApplicable=None, dontKnow=None
                 ):
        self.__notApplicable = notApplicable
        self.__dontKnow = dontKnow

    def _get_notApplicable(self):
        return self.__notApplicable

    def _set_notApplicable(self, value):
        if not isinstance(value, list):
            raise TypeError("notApplicable must be list")
        self.__notApplicable = value
    notApplicable = property(_get_notApplicable, _set_notApplicable)

    def _get_dontKnow(self):
        return self.__dontKnow

    def _set_dontKnow(self, value):
        if not isinstance(value, list):
            raise TypeError("dontKnow must be list")
        self.__dontKnow = value
    dontKnow = property(_get_dontKnow, _set_dontKnow)

    def as_dict(self):
        d = dict()
        if self.__notApplicable is not None:
            d['notApplicable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__notApplicable]
        if self.__dontKnow is not None:
            d['dontKnow'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dontKnow]
        return d


class Proposed:

    _types_map = {
        'content': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, content=None
                 ):
        self.__content = content

    def _get_content(self):
        return self.__content

    def _set_content(self, value):
        if not isinstance(value, list):
            raise TypeError("content must be list")
        self.__content = value
    content = property(_get_content, _set_content)

    def as_dict(self):
        d = dict()
        if self.__content is not None:
            d['content'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__content]
        return d


class FaxNationalNumber:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class RoomInformation:

    _types_map = {
        'existingRoomsToBeLost': {'type': list, 'subtype': None},
        'totalRoomsProposed': {'type': list, 'subtype': None},
        'netAdditionalRooms': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existingRoomsToBeLost=None, totalRoomsProposed=None, netAdditionalRooms=None
                 ):
        self.__existingRoomsToBeLost = existingRoomsToBeLost
        self.__totalRoomsProposed = totalRoomsProposed
        self.__netAdditionalRooms = netAdditionalRooms

    def _get_existingRoomsToBeLost(self):
        return self.__existingRoomsToBeLost

    def _set_existingRoomsToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("existingRoomsToBeLost must be list")
        self.__existingRoomsToBeLost = value
    existingRoomsToBeLost = property(_get_existingRoomsToBeLost, _set_existingRoomsToBeLost)

    def _get_totalRoomsProposed(self):
        return self.__totalRoomsProposed

    def _set_totalRoomsProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalRoomsProposed must be list")
        self.__totalRoomsProposed = value
    totalRoomsProposed = property(_get_totalRoomsProposed, _set_totalRoomsProposed)

    def _get_netAdditionalRooms(self):
        return self.__netAdditionalRooms

    def _set_netAdditionalRooms(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalRooms must be list")
        self.__netAdditionalRooms = value
    netAdditionalRooms = property(_get_netAdditionalRooms, _set_netAdditionalRooms)

    def as_dict(self):
        d = dict()
        if self.__existingRoomsToBeLost is not None:
            d['existingRoomsToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingRoomsToBeLost]
        if self.__totalRoomsProposed is not None:
            d['totalRoomsProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalRoomsProposed]
        if self.__netAdditionalRooms is not None:
            d['netAdditionalRooms'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalRooms]
        return d


class CommercialIndustrial:

    _types_map = {
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, maxAnnualOperationalThroughput=None
                 ):
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class Agent:

    _types_map = {
        'personName': {'type': list, 'subtype': None},
        'orgName': {'type': list, 'subtype': None},
        'externalAddress': {'type': list, 'subtype': None},
        'contactDetails': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, personName=None, orgName=None, externalAddress=None, contactDetails=None
                 ):
        self.__personName = personName
        self.__orgName = orgName
        self.__externalAddress = externalAddress
        self.__contactDetails = contactDetails

    def _get_personName(self):
        return self.__personName

    def _set_personName(self, value):
        if not isinstance(value, list):
            raise TypeError("personName must be list")
        self.__personName = value
    personName = property(_get_personName, _set_personName)

    def _get_orgName(self):
        return self.__orgName

    def _set_orgName(self, value):
        if not isinstance(value, list):
            raise TypeError("orgName must be list")
        self.__orgName = value
    orgName = property(_get_orgName, _set_orgName)

    def _get_externalAddress(self):
        return self.__externalAddress

    def _set_externalAddress(self, value):
        if not isinstance(value, list):
            raise TypeError("externalAddress must be list")
        self.__externalAddress = value
    externalAddress = property(_get_externalAddress, _set_externalAddress)

    def _get_contactDetails(self):
        return self.__contactDetails

    def _set_contactDetails(self, value):
        if not isinstance(value, list):
            raise TypeError("contactDetails must be list")
        self.__contactDetails = value
    contactDetails = property(_get_contactDetails, _set_contactDetails)

    def as_dict(self):
        d = dict()
        if self.__personName is not None:
            d['personName'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__personName]
        if self.__orgName is not None:
            d['orgName'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__orgName]
        if self.__externalAddress is not None:
            d['externalAddress'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__externalAddress]
        if self.__contactDetails is not None:
            d['contactDetails'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__contactDetails]
        return d


class Other:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        'proposed': {'type': list, 'subtype': None},
        'notApplicable': {'type': list, 'subtype': None},
        'dontKnow': {'type': list, 'subtype': None},
        'specifiedOther': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
        'roomInformation': {'type': list, 'subtype': None},
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, proposed=None, notApplicable=None, dontKnow=None, specifiedOther=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None, roomInformation=None, monToFri=None, sat=None, sunBH=None
                 ):
        self.__existing = existing
        self.__proposed = proposed
        self.__notApplicable = notApplicable
        self.__dontKnow = dontKnow
        self.__specifiedOther = specifiedOther
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace
        self.__roomInformation = roomInformation
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get_proposed(self):
        return self.__proposed

    def _set_proposed(self, value):
        if not isinstance(value, list):
            raise TypeError("proposed must be list")
        self.__proposed = value
    proposed = property(_get_proposed, _set_proposed)

    def _get_notApplicable(self):
        return self.__notApplicable

    def _set_notApplicable(self, value):
        if not isinstance(value, list):
            raise TypeError("notApplicable must be list")
        self.__notApplicable = value
    notApplicable = property(_get_notApplicable, _set_notApplicable)

    def _get_dontKnow(self):
        return self.__dontKnow

    def _set_dontKnow(self, value):
        if not isinstance(value, list):
            raise TypeError("dontKnow must be list")
        self.__dontKnow = value
    dontKnow = property(_get_dontKnow, _set_dontKnow)

    def _get_specifiedOther(self):
        return self.__specifiedOther

    def _set_specifiedOther(self, value):
        if not isinstance(value, list):
            raise TypeError("specifiedOther must be list")
        self.__specifiedOther = value
    specifiedOther = property(_get_specifiedOther, _set_specifiedOther)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def _get_roomInformation(self):
        return self.__roomInformation

    def _set_roomInformation(self, value):
        if not isinstance(value, list):
            raise TypeError("roomInformation must be list")
        self.__roomInformation = value
    roomInformation = property(_get_roomInformation, _set_roomInformation)

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.__proposed is not None:
            d['proposed'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__proposed]
        if self.__notApplicable is not None:
            d['notApplicable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__notApplicable]
        if self.__dontKnow is not None:
            d['dontKnow'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dontKnow]
        if self.__specifiedOther is not None:
            d['specifiedOther'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__specifiedOther]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        if self.__roomInformation is not None:
            d['roomInformation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__roomInformation]
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        return d


class ExistingUse:

    _types_map = {
        'currentUse': {'type': list, 'subtype': None},
        'isCurrentlyVacant': {'type': list, 'subtype': None},
        'lastUse': {'type': list, 'subtype': None},
        'contaminatedLandKnown': {'type': list, 'subtype': None},
        'contaminatedLandSuspect': {'type': list, 'subtype': None},
        'contaminatedProposedUse': {'type': list, 'subtype': None},
        'constructingNewBuilding': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, currentUse=None, isCurrentlyVacant=None, lastUse=None, contaminatedLandKnown=None, contaminatedLandSuspect=None, contaminatedProposedUse=None, constructingNewBuilding=None
                 ):
        self.__currentUse = currentUse
        self.__isCurrentlyVacant = isCurrentlyVacant
        self.__lastUse = lastUse
        self.__contaminatedLandKnown = contaminatedLandKnown
        self.__contaminatedLandSuspect = contaminatedLandSuspect
        self.__contaminatedProposedUse = contaminatedProposedUse
        self.__constructingNewBuilding = constructingNewBuilding

    def _get_currentUse(self):
        return self.__currentUse

    def _set_currentUse(self, value):
        if not isinstance(value, list):
            raise TypeError("currentUse must be list")
        self.__currentUse = value
    currentUse = property(_get_currentUse, _set_currentUse)

    def _get_isCurrentlyVacant(self):
        return self.__isCurrentlyVacant

    def _set_isCurrentlyVacant(self, value):
        if not isinstance(value, list):
            raise TypeError("isCurrentlyVacant must be list")
        self.__isCurrentlyVacant = value
    isCurrentlyVacant = property(_get_isCurrentlyVacant, _set_isCurrentlyVacant)

    def _get_lastUse(self):
        return self.__lastUse

    def _set_lastUse(self, value):
        if not isinstance(value, list):
            raise TypeError("lastUse must be list")
        self.__lastUse = value
    lastUse = property(_get_lastUse, _set_lastUse)

    def _get_contaminatedLandKnown(self):
        return self.__contaminatedLandKnown

    def _set_contaminatedLandKnown(self, value):
        if not isinstance(value, list):
            raise TypeError("contaminatedLandKnown must be list")
        self.__contaminatedLandKnown = value
    contaminatedLandKnown = property(_get_contaminatedLandKnown, _set_contaminatedLandKnown)

    def _get_contaminatedLandSuspect(self):
        return self.__contaminatedLandSuspect

    def _set_contaminatedLandSuspect(self, value):
        if not isinstance(value, list):
            raise TypeError("contaminatedLandSuspect must be list")
        self.__contaminatedLandSuspect = value
    contaminatedLandSuspect = property(_get_contaminatedLandSuspect, _set_contaminatedLandSuspect)

    def _get_contaminatedProposedUse(self):
        return self.__contaminatedProposedUse

    def _set_contaminatedProposedUse(self, value):
        if not isinstance(value, list):
            raise TypeError("contaminatedProposedUse must be list")
        self.__contaminatedProposedUse = value
    contaminatedProposedUse = property(_get_contaminatedProposedUse, _set_contaminatedProposedUse)

    def _get_constructingNewBuilding(self):
        return self.__constructingNewBuilding

    def _set_constructingNewBuilding(self, value):
        if not isinstance(value, list):
            raise TypeError("constructingNewBuilding must be list")
        self.__constructingNewBuilding = value
    constructingNewBuilding = property(_get_constructingNewBuilding, _set_constructingNewBuilding)

    def as_dict(self):
        d = dict()
        if self.__currentUse is not None:
            d['currentUse'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__currentUse]
        if self.__isCurrentlyVacant is not None:
            d['isCurrentlyVacant'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__isCurrentlyVacant]
        if self.__lastUse is not None:
            d['lastUse'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__lastUse]
        if self.__contaminatedLandKnown is not None:
            d['contaminatedLandKnown'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__contaminatedLandKnown]
        if self.__contaminatedLandSuspect is not None:
            d['contaminatedLandSuspect'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__contaminatedLandSuspect]
        if self.__contaminatedProposedUse is not None:
            d['contaminatedProposedUse'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__contaminatedProposedUse]
        if self.__constructingNewBuilding is not None:
            d['constructingNewBuilding'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__constructingNewBuilding]
        return d


class TransferStations:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class InternationalAddress:

    _types_map = {
        'intAddressLine': {'type': list, 'subtype': None},
        'countryOrInternationalPostCode': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, intAddressLine=None, countryOrInternationalPostCode=None
                 ):
        self.__intAddressLine = intAddressLine
        self.__countryOrInternationalPostCode = countryOrInternationalPostCode

    def _get_intAddressLine(self):
        return self.__intAddressLine

    def _set_intAddressLine(self, value):
        if not isinstance(value, list):
            raise TypeError("intAddressLine must be list")
        self.__intAddressLine = value
    intAddressLine = property(_get_intAddressLine, _set_intAddressLine)

    def _get_countryOrInternationalPostCode(self):
        return self.__countryOrInternationalPostCode

    def _set_countryOrInternationalPostCode(self, value):
        if not isinstance(value, list):
            raise TypeError("countryOrInternationalPostCode must be list")
        self.__countryOrInternationalPostCode = value
    countryOrInternationalPostCode = property(
        _get_countryOrInternationalPostCode, _set_countryOrInternationalPostCode)

    def as_dict(self):
        d = dict()
        if self.__intAddressLine is not None:
            d['intAddressLine'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__intAddressLine]
        if self.__countryOrInternationalPostCode is not None:
            d['countryOrInternationalPostCode'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__countryOrInternationalPostCode]
        return d


class TradeEffluent:

    _types_map = {
        'disposeTradeWaste': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, disposeTradeWaste=None
                 ):
        self.__disposeTradeWaste = disposeTradeWaste

    def _get_disposeTradeWaste(self):
        return self.__disposeTradeWaste

    def _set_disposeTradeWaste(self, value):
        if not isinstance(value, list):
            raise TypeError("disposeTradeWaste must be list")
        self.__disposeTradeWaste = value
    disposeTradeWaste = property(_get_disposeTradeWaste, _set_disposeTradeWaste)

    def as_dict(self):
        d = dict()
        if self.__disposeTradeWaste is not None:
            d['disposeTradeWaste'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__disposeTradeWaste]
        return d


class Access:

    _types_map = {
        'newAlteredVehicular': {'type': list, 'subtype': None},
        'newAlteredPedestrian': {'type': list, 'subtype': None},
        'newRightsOfWay': {'type': list, 'subtype': None},
        'newPublicRoad': {'type': list, 'subtype': None},
        'changeRightsOfWay': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, newAlteredVehicular=None, newAlteredPedestrian=None, newRightsOfWay=None, newPublicRoad=None, changeRightsOfWay=None
                 ):
        self.__newAlteredVehicular = newAlteredVehicular
        self.__newAlteredPedestrian = newAlteredPedestrian
        self.__newRightsOfWay = newRightsOfWay
        self.__newPublicRoad = newPublicRoad
        self.__changeRightsOfWay = changeRightsOfWay

    def _get_newAlteredVehicular(self):
        return self.__newAlteredVehicular

    def _set_newAlteredVehicular(self, value):
        if not isinstance(value, list):
            raise TypeError("newAlteredVehicular must be list")
        self.__newAlteredVehicular = value
    newAlteredVehicular = property(_get_newAlteredVehicular, _set_newAlteredVehicular)

    def _get_newAlteredPedestrian(self):
        return self.__newAlteredPedestrian

    def _set_newAlteredPedestrian(self, value):
        if not isinstance(value, list):
            raise TypeError("newAlteredPedestrian must be list")
        self.__newAlteredPedestrian = value
    newAlteredPedestrian = property(_get_newAlteredPedestrian, _set_newAlteredPedestrian)

    def _get_newRightsOfWay(self):
        return self.__newRightsOfWay

    def _set_newRightsOfWay(self, value):
        if not isinstance(value, list):
            raise TypeError("newRightsOfWay must be list")
        self.__newRightsOfWay = value
    newRightsOfWay = property(_get_newRightsOfWay, _set_newRightsOfWay)

    def _get_newPublicRoad(self):
        return self.__newPublicRoad

    def _set_newPublicRoad(self, value):
        if not isinstance(value, list):
            raise TypeError("newPublicRoad must be list")
        self.__newPublicRoad = value
    newPublicRoad = property(_get_newPublicRoad, _set_newPublicRoad)

    def _get_changeRightsOfWay(self):
        return self.__changeRightsOfWay

    def _set_changeRightsOfWay(self, value):
        if not isinstance(value, list):
            raise TypeError("changeRightsOfWay must be list")
        self.__changeRightsOfWay = value
    changeRightsOfWay = property(_get_changeRightsOfWay, _set_changeRightsOfWay)

    def as_dict(self):
        d = dict()
        if self.__newAlteredVehicular is not None:
            d['newAlteredVehicular'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__newAlteredVehicular]
        if self.__newAlteredPedestrian is not None:
            d['newAlteredPedestrian'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__newAlteredPedestrian]
        if self.__newRightsOfWay is not None:
            d['newRightsOfWay'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__newRightsOfWay]
        if self.__newPublicRoad is not None:
            d['newPublicRoad'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__newPublicRoad]
        if self.__changeRightsOfWay is not None:
            d['changeRightsOfWay'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__changeRightsOfWay]
        return d


class PublicationName:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class Materials:

    _types_map = {
        'roof': {'type': list, 'subtype': None},
        'windows': {'type': list, 'subtype': None},
        'boundaries': {'type': list, 'subtype': None},
        'vehicleAccess': {'type': list, 'subtype': None},
        'lighting': {'type': list, 'subtype': None},
        'externalWalls': {'type': list, 'subtype': None},
        'externalDoors': {'type': list, 'subtype': None},
        'other': {'type': list, 'subtype': None},
        'supportingInformation': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, roof=None, windows=None, boundaries=None, vehicleAccess=None, lighting=None, externalWalls=None, externalDoors=None, other=None, supportingInformation=None
                 ):
        self.__roof = roof
        self.__windows = windows
        self.__boundaries = boundaries
        self.__vehicleAccess = vehicleAccess
        self.__lighting = lighting
        self.__externalWalls = externalWalls
        self.__externalDoors = externalDoors
        self.__other = other
        self.__supportingInformation = supportingInformation

    def _get_roof(self):
        return self.__roof

    def _set_roof(self, value):
        if not isinstance(value, list):
            raise TypeError("roof must be list")
        self.__roof = value
    roof = property(_get_roof, _set_roof)

    def _get_windows(self):
        return self.__windows

    def _set_windows(self, value):
        if not isinstance(value, list):
            raise TypeError("windows must be list")
        self.__windows = value
    windows = property(_get_windows, _set_windows)

    def _get_boundaries(self):
        return self.__boundaries

    def _set_boundaries(self, value):
        if not isinstance(value, list):
            raise TypeError("boundaries must be list")
        self.__boundaries = value
    boundaries = property(_get_boundaries, _set_boundaries)

    def _get_vehicleAccess(self):
        return self.__vehicleAccess

    def _set_vehicleAccess(self, value):
        if not isinstance(value, list):
            raise TypeError("vehicleAccess must be list")
        self.__vehicleAccess = value
    vehicleAccess = property(_get_vehicleAccess, _set_vehicleAccess)

    def _get_lighting(self):
        return self.__lighting

    def _set_lighting(self, value):
        if not isinstance(value, list):
            raise TypeError("lighting must be list")
        self.__lighting = value
    lighting = property(_get_lighting, _set_lighting)

    def _get_externalWalls(self):
        return self.__externalWalls

    def _set_externalWalls(self, value):
        if not isinstance(value, list):
            raise TypeError("externalWalls must be list")
        self.__externalWalls = value
    externalWalls = property(_get_externalWalls, _set_externalWalls)

    def _get_externalDoors(self):
        return self.__externalDoors

    def _set_externalDoors(self, value):
        if not isinstance(value, list):
            raise TypeError("externalDoors must be list")
        self.__externalDoors = value
    externalDoors = property(_get_externalDoors, _set_externalDoors)

    def _get_other(self):
        return self.__other

    def _set_other(self, value):
        if not isinstance(value, list):
            raise TypeError("other must be list")
        self.__other = value
    other = property(_get_other, _set_other)

    def _get_supportingInformation(self):
        return self.__supportingInformation

    def _set_supportingInformation(self, value):
        if not isinstance(value, list):
            raise TypeError("supportingInformation must be list")
        self.__supportingInformation = value
    supportingInformation = property(_get_supportingInformation, _set_supportingInformation)

    def as_dict(self):
        d = dict()
        if self.__roof is not None:
            d['roof'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__roof]
        if self.__windows is not None:
            d['windows'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__windows]
        if self.__boundaries is not None:
            d['boundaries'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__boundaries]
        if self.__vehicleAccess is not None:
            d['vehicleAccess'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__vehicleAccess]
        if self.__lighting is not None:
            d['lighting'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__lighting]
        if self.__externalWalls is not None:
            d['externalWalls'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__externalWalls]
        if self.__externalDoors is not None:
            d['externalDoors'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__externalDoors]
        if self.__other is not None:
            d['other'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__other]
        if self.__supportingInformation is not None:
            d['supportingInformation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__supportingInformation]
        return d


class ApplicationData:

    _types_map = {
        'proposalDescription': {'type': list, 'subtype': None},
        'siteArea': {'type': list, 'subtype': None},
        'existingUse': {'type': list, 'subtype': None},
        'residentialDevelopment': {'type': list, 'subtype': None},
        'nonResidentialDevelopment': {'type': list, 'subtype': None},
        'employment': {'type': list, 'subtype': None},
        'hours': {'type': list, 'subtype': None},
        'industrialCommercial': {'type': list, 'subtype': None},
        'hazardousSubstances': {'type': list, 'subtype': None},
        'tradeEffluent': {'type': list, 'subtype': None},
        'access': {'type': list, 'subtype': None},
        'parking': {'type': list, 'subtype': None},
        'materials': {'type': list, 'subtype': None},
        'foulSewage': {'type': list, 'subtype': None},
        'floodRisk': {'type': list, 'subtype': None},
        'allTreesHedges': {'type': list, 'subtype': None},
        'wasteStorageCollection': {'type': list, 'subtype': None},
        'advice': {'type': list, 'subtype': None},
        'siteVisit': {'type': list, 'subtype': None},
        'ownershipCertificates': {'type': list, 'subtype': None},
        'biodiversity': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, proposalDescription=None, siteArea=None, existingUse=None, residentialDevelopment=None, nonResidentialDevelopment=None, employment=None, hours=None, industrialCommercial=None, hazardousSubstances=None, tradeEffluent=None, access=None, parking=None, materials=None, foulSewage=None, floodRisk=None, allTreesHedges=None, wasteStorageCollection=None, advice=None, siteVisit=None, ownershipCertificates=None, biodiversity=None
                 ):
        self.__proposalDescription = proposalDescription
        self.__siteArea = siteArea
        self.__existingUse = existingUse
        self.__residentialDevelopment = residentialDevelopment
        self.__nonResidentialDevelopment = nonResidentialDevelopment
        self.__employment = employment
        self.__hours = hours
        self.__industrialCommercial = industrialCommercial
        self.__hazardousSubstances = hazardousSubstances
        self.__tradeEffluent = tradeEffluent
        self.__access = access
        self.__parking = parking
        self.__materials = materials
        self.__foulSewage = foulSewage
        self.__floodRisk = floodRisk
        self.__allTreesHedges = allTreesHedges
        self.__wasteStorageCollection = wasteStorageCollection
        self.__advice = advice
        self.__siteVisit = siteVisit
        self.__ownershipCertificates = ownershipCertificates
        self.__biodiversity = biodiversity

    def _get_proposalDescription(self):
        return self.__proposalDescription

    def _set_proposalDescription(self, value):
        if not isinstance(value, list):
            raise TypeError("proposalDescription must be list")
        self.__proposalDescription = value
    proposalDescription = property(_get_proposalDescription, _set_proposalDescription)

    def _get_siteArea(self):
        return self.__siteArea

    def _set_siteArea(self, value):
        if not isinstance(value, list):
            raise TypeError("siteArea must be list")
        self.__siteArea = value
    siteArea = property(_get_siteArea, _set_siteArea)

    def _get_existingUse(self):
        return self.__existingUse

    def _set_existingUse(self, value):
        if not isinstance(value, list):
            raise TypeError("existingUse must be list")
        self.__existingUse = value
    existingUse = property(_get_existingUse, _set_existingUse)

    def _get_residentialDevelopment(self):
        return self.__residentialDevelopment

    def _set_residentialDevelopment(self, value):
        if not isinstance(value, list):
            raise TypeError("residentialDevelopment must be list")
        self.__residentialDevelopment = value
    residentialDevelopment = property(_get_residentialDevelopment, _set_residentialDevelopment)

    def _get_nonResidentialDevelopment(self):
        return self.__nonResidentialDevelopment

    def _set_nonResidentialDevelopment(self, value):
        if not isinstance(value, list):
            raise TypeError("nonResidentialDevelopment must be list")
        self.__nonResidentialDevelopment = value
    nonResidentialDevelopment = property(
        _get_nonResidentialDevelopment, _set_nonResidentialDevelopment)

    def _get_employment(self):
        return self.__employment

    def _set_employment(self, value):
        if not isinstance(value, list):
            raise TypeError("employment must be list")
        self.__employment = value
    employment = property(_get_employment, _set_employment)

    def _get_hours(self):
        return self.__hours

    def _set_hours(self, value):
        if not isinstance(value, list):
            raise TypeError("hours must be list")
        self.__hours = value
    hours = property(_get_hours, _set_hours)

    def _get_industrialCommercial(self):
        return self.__industrialCommercial

    def _set_industrialCommercial(self, value):
        if not isinstance(value, list):
            raise TypeError("industrialCommercial must be list")
        self.__industrialCommercial = value
    industrialCommercial = property(_get_industrialCommercial, _set_industrialCommercial)

    def _get_hazardousSubstances(self):
        return self.__hazardousSubstances

    def _set_hazardousSubstances(self, value):
        if not isinstance(value, list):
            raise TypeError("hazardousSubstances must be list")
        self.__hazardousSubstances = value
    hazardousSubstances = property(_get_hazardousSubstances, _set_hazardousSubstances)

    def _get_tradeEffluent(self):
        return self.__tradeEffluent

    def _set_tradeEffluent(self, value):
        if not isinstance(value, list):
            raise TypeError("tradeEffluent must be list")
        self.__tradeEffluent = value
    tradeEffluent = property(_get_tradeEffluent, _set_tradeEffluent)

    def _get_access(self):
        return self.__access

    def _set_access(self, value):
        if not isinstance(value, list):
            raise TypeError("access must be list")
        self.__access = value
    access = property(_get_access, _set_access)

    def _get_parking(self):
        return self.__parking

    def _set_parking(self, value):
        if not isinstance(value, list):
            raise TypeError("parking must be list")
        self.__parking = value
    parking = property(_get_parking, _set_parking)

    def _get_materials(self):
        return self.__materials

    def _set_materials(self, value):
        if not isinstance(value, list):
            raise TypeError("materials must be list")
        self.__materials = value
    materials = property(_get_materials, _set_materials)

    def _get_foulSewage(self):
        return self.__foulSewage

    def _set_foulSewage(self, value):
        if not isinstance(value, list):
            raise TypeError("foulSewage must be list")
        self.__foulSewage = value
    foulSewage = property(_get_foulSewage, _set_foulSewage)

    def _get_floodRisk(self):
        return self.__floodRisk

    def _set_floodRisk(self, value):
        if not isinstance(value, list):
            raise TypeError("floodRisk must be list")
        self.__floodRisk = value
    floodRisk = property(_get_floodRisk, _set_floodRisk)

    def _get_allTreesHedges(self):
        return self.__allTreesHedges

    def _set_allTreesHedges(self, value):
        if not isinstance(value, list):
            raise TypeError("allTreesHedges must be list")
        self.__allTreesHedges = value
    allTreesHedges = property(_get_allTreesHedges, _set_allTreesHedges)

    def _get_wasteStorageCollection(self):
        return self.__wasteStorageCollection

    def _set_wasteStorageCollection(self, value):
        if not isinstance(value, list):
            raise TypeError("wasteStorageCollection must be list")
        self.__wasteStorageCollection = value
    wasteStorageCollection = property(_get_wasteStorageCollection, _set_wasteStorageCollection)

    def _get_advice(self):
        return self.__advice

    def _set_advice(self, value):
        if not isinstance(value, list):
            raise TypeError("advice must be list")
        self.__advice = value
    advice = property(_get_advice, _set_advice)

    def _get_siteVisit(self):
        return self.__siteVisit

    def _set_siteVisit(self, value):
        if not isinstance(value, list):
            raise TypeError("siteVisit must be list")
        self.__siteVisit = value
    siteVisit = property(_get_siteVisit, _set_siteVisit)

    def _get_ownershipCertificates(self):
        return self.__ownershipCertificates

    def _set_ownershipCertificates(self, value):
        if not isinstance(value, list):
            raise TypeError("ownershipCertificates must be list")
        self.__ownershipCertificates = value
    ownershipCertificates = property(_get_ownershipCertificates, _set_ownershipCertificates)

    def _get_biodiversity(self):
        return self.__biodiversity

    def _set_biodiversity(self, value):
        if not isinstance(value, list):
            raise TypeError("biodiversity must be list")
        self.__biodiversity = value
    biodiversity = property(_get_biodiversity, _set_biodiversity)

    def as_dict(self):
        d = dict()
        if self.__proposalDescription is not None:
            d['proposalDescription'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__proposalDescription]
        if self.__siteArea is not None:
            d['siteArea'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__siteArea]
        if self.__existingUse is not None:
            d['existingUse'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existingUse]
        if self.__residentialDevelopment is not None:
            d['residentialDevelopment'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__residentialDevelopment]
        if self.__nonResidentialDevelopment is not None:
            d['nonResidentialDevelopment'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__nonResidentialDevelopment]
        if self.__employment is not None:
            d['employment'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__employment]
        if self.__hours is not None:
            d['hours'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__hours]
        if self.__industrialCommercial is not None:
            d['industrialCommercial'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__industrialCommercial]
        if self.__hazardousSubstances is not None:
            d['hazardousSubstances'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__hazardousSubstances]
        if self.__tradeEffluent is not None:
            d['tradeEffluent'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__tradeEffluent]
        if self.__access is not None:
            d['access'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__access]
        if self.__parking is not None:
            d['parking'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__parking]
        if self.__materials is not None:
            d['materials'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__materials]
        if self.__foulSewage is not None:
            d['foulSewage'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__foulSewage]
        if self.__floodRisk is not None:
            d['floodRisk'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__floodRisk]
        if self.__allTreesHedges is not None:
            d['allTreesHedges'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__allTreesHedges]
        if self.__wasteStorageCollection is not None:
            d['wasteStorageCollection'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__wasteStorageCollection]
        if self.__advice is not None:
            d['advice'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__advice]
        if self.__siteVisit is not None:
            d['siteVisit'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__siteVisit]
        if self.__ownershipCertificates is not None:
            d['ownershipCertificates'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__ownershipCertificates]
        if self.__biodiversity is not None:
            d['biodiversity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__biodiversity]
        return d


class A4:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class Totals:

    _types_map = {
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class B1A:

    _types_map = {
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None, monToFri=None, sat=None, sunBH=None
                 ):
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def as_dict(self):
        d = dict()
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        return d


class ApplicationHeader:

    _types_map = {
        'applicationTo': {'type': list, 'subtype': None},
        'dateSubmitted': {'type': list, 'subtype': None},
        'refNum': {'type': list, 'subtype': None},
        'formattedRefNum': {'type': list, 'subtype': None},
        'applicationVersion': {'type': list, 'subtype': None},
        'attachmentsChanged': {'type': list, 'subtype': None},
        'description': {'type': list, 'subtype': None},
        'payment': {'type': list, 'subtype': None},
        'isValidApplication': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, applicationTo=None, dateSubmitted=None, refNum=None, formattedRefNum=None, applicationVersion=None, attachmentsChanged=None, description=None, payment=None, isValidApplication=None
                 ):
        self.__applicationTo = applicationTo
        self.__dateSubmitted = dateSubmitted
        self.__refNum = refNum
        self.__formattedRefNum = formattedRefNum
        self.__applicationVersion = applicationVersion
        self.__attachmentsChanged = attachmentsChanged
        self.__description = description
        self.__payment = payment
        self.__isValidApplication = isValidApplication

    def _get_applicationTo(self):
        return self.__applicationTo

    def _set_applicationTo(self, value):
        if not isinstance(value, list):
            raise TypeError("applicationTo must be list")
        self.__applicationTo = value
    applicationTo = property(_get_applicationTo, _set_applicationTo)

    def _get_dateSubmitted(self):
        return self.__dateSubmitted

    def _set_dateSubmitted(self, value):
        if not isinstance(value, list):
            raise TypeError("dateSubmitted must be list")
        self.__dateSubmitted = value
    dateSubmitted = property(_get_dateSubmitted, _set_dateSubmitted)

    def _get_refNum(self):
        return self.__refNum

    def _set_refNum(self, value):
        if not isinstance(value, list):
            raise TypeError("refNum must be list")
        self.__refNum = value
    refNum = property(_get_refNum, _set_refNum)

    def _get_formattedRefNum(self):
        return self.__formattedRefNum

    def _set_formattedRefNum(self, value):
        if not isinstance(value, list):
            raise TypeError("formattedRefNum must be list")
        self.__formattedRefNum = value
    formattedRefNum = property(_get_formattedRefNum, _set_formattedRefNum)

    def _get_applicationVersion(self):
        return self.__applicationVersion

    def _set_applicationVersion(self, value):
        if not isinstance(value, list):
            raise TypeError("applicationVersion must be list")
        self.__applicationVersion = value
    applicationVersion = property(_get_applicationVersion, _set_applicationVersion)

    def _get_attachmentsChanged(self):
        return self.__attachmentsChanged

    def _set_attachmentsChanged(self, value):
        if not isinstance(value, list):
            raise TypeError("attachmentsChanged must be list")
        self.__attachmentsChanged = value
    attachmentsChanged = property(_get_attachmentsChanged, _set_attachmentsChanged)

    def _get_description(self):
        return self.__description

    def _set_description(self, value):
        if not isinstance(value, list):
            raise TypeError("description must be list")
        self.__description = value
    description = property(_get_description, _set_description)

    def _get_payment(self):
        return self.__payment

    def _set_payment(self, value):
        if not isinstance(value, list):
            raise TypeError("payment must be list")
        self.__payment = value
    payment = property(_get_payment, _set_payment)

    def _get_isValidApplication(self):
        return self.__isValidApplication

    def _set_isValidApplication(self, value):
        if not isinstance(value, list):
            raise TypeError("isValidApplication must be list")
        self.__isValidApplication = value
    isValidApplication = property(_get_isValidApplication, _set_isValidApplication)

    def as_dict(self):
        d = dict()
        if self.__applicationTo is not None:
            d['applicationTo'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__applicationTo]
        if self.__dateSubmitted is not None:
            d['dateSubmitted'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__dateSubmitted]
        if self.__refNum is not None:
            d['refNum'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__refNum]
        if self.__formattedRefNum is not None:
            d['formattedRefNum'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__formattedRefNum]
        if self.__applicationVersion is not None:
            d['applicationVersion'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__applicationVersion]
        if self.__attachmentsChanged is not None:
            d['attachmentsChanged'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__attachmentsChanged]
        if self.__description is not None:
            d['description'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__description]
        if self.__payment is not None:
            d['payment'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__payment]
        if self.__isValidApplication is not None:
            d['isValidApplication'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__isValidApplication]
        return d


class AdviceDetails:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class SpecifiedOther:

    _types_map = {
        'content': {'type': list, 'subtype': None},
        'otherCode': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, content=None, otherCode=None
                 ):
        self.__content = content
        self.__otherCode = otherCode

    def _get_content(self):
        return self.__content

    def _set_content(self, value):
        if not isinstance(value, list):
            raise TypeError("content must be list")
        self.__content = value
    content = property(_get_content, _set_content)

    def _get_otherCode(self):
        return self.__otherCode

    def _set_otherCode(self, value):
        if not isinstance(value, list):
            raise TypeError("otherCode must be list")
        self.__otherCode = value
    otherCode = property(_get_otherCode, _set_otherCode)

    def as_dict(self):
        d = dict()
        if self.__content is not None:
            d['content'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__content]
        if self.__otherCode is not None:
            d['otherCode'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__otherCode]
        return d


class HazardousLandfill:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class OwnershipCertificates:

    _types_map = {
        'certificateSelected': {'type': list, 'subtype': None},
        'noticeGiven': {'type': list, 'subtype': None},
        'advertisement': {'type': list, 'subtype': None},
        'ownershipDeclaration': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, certificateSelected=None, noticeGiven=None, advertisement=None, ownershipDeclaration=None
                 ):
        self.__certificateSelected = certificateSelected
        self.__noticeGiven = noticeGiven
        self.__advertisement = advertisement
        self.__ownershipDeclaration = ownershipDeclaration

    def _get_certificateSelected(self):
        return self.__certificateSelected

    def _set_certificateSelected(self, value):
        if not isinstance(value, list):
            raise TypeError("certificateSelected must be list")
        self.__certificateSelected = value
    certificateSelected = property(_get_certificateSelected, _set_certificateSelected)

    def _get_noticeGiven(self):
        return self.__noticeGiven

    def _set_noticeGiven(self, value):
        if not isinstance(value, list):
            raise TypeError("noticeGiven must be list")
        self.__noticeGiven = value
    noticeGiven = property(_get_noticeGiven, _set_noticeGiven)

    def _get_advertisement(self):
        return self.__advertisement

    def _set_advertisement(self, value):
        if not isinstance(value, list):
            raise TypeError("advertisement must be list")
        self.__advertisement = value
    advertisement = property(_get_advertisement, _set_advertisement)

    def _get_ownershipDeclaration(self):
        return self.__ownershipDeclaration

    def _set_ownershipDeclaration(self, value):
        if not isinstance(value, list):
            raise TypeError("ownershipDeclaration must be list")
        self.__ownershipDeclaration = value
    ownershipDeclaration = property(_get_ownershipDeclaration, _set_ownershipDeclaration)

    def as_dict(self):
        d = dict()
        if self.__certificateSelected is not None:
            d['certificateSelected'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__certificateSelected]
        if self.__noticeGiven is not None:
            d['noticeGiven'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__noticeGiven]
        if self.__advertisement is not None:
            d['advertisement'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__advertisement]
        if self.__ownershipDeclaration is not None:
            d['ownershipDeclaration'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__ownershipDeclaration]
        return d


class Biodiversity:

    _types_map = {
        'protectedPrioritySpecies': {'type': list, 'subtype': None},
        'designatedSites': {'type': list, 'subtype': None},
        'geologicalConservationImportance': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, protectedPrioritySpecies=None, designatedSites=None, geologicalConservationImportance=None
                 ):
        self.__protectedPrioritySpecies = protectedPrioritySpecies
        self.__designatedSites = designatedSites
        self.__geologicalConservationImportance = geologicalConservationImportance

    def _get_protectedPrioritySpecies(self):
        return self.__protectedPrioritySpecies

    def _set_protectedPrioritySpecies(self, value):
        if not isinstance(value, list):
            raise TypeError("protectedPrioritySpecies must be list")
        self.__protectedPrioritySpecies = value
    protectedPrioritySpecies = property(
        _get_protectedPrioritySpecies, _set_protectedPrioritySpecies)

    def _get_designatedSites(self):
        return self.__designatedSites

    def _set_designatedSites(self, value):
        if not isinstance(value, list):
            raise TypeError("designatedSites must be list")
        self.__designatedSites = value
    designatedSites = property(_get_designatedSites, _set_designatedSites)

    def _get_geologicalConservationImportance(self):
        return self.__geologicalConservationImportance

    def _set_geologicalConservationImportance(self, value):
        if not isinstance(value, list):
            raise TypeError("geologicalConservationImportance must be list")
        self.__geologicalConservationImportance = value
    geologicalConservationImportance = property(
        _get_geologicalConservationImportance, _set_geologicalConservationImportance)

    def as_dict(self):
        d = dict()
        if self.__protectedPrioritySpecies is not None:
            d['protectedPrioritySpecies'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__protectedPrioritySpecies]
        if self.__designatedSites is not None:
            d['designatedSites'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__designatedSites]
        if self.__geologicalConservationImportance is not None:
            d['geologicalConservationImportance'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__geologicalConservationImportance]
        return d


class Cars:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        '_new': {'type': list, 'subtype': None},
        'difference': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, _new=None, difference=None
                 ):
        self.__existing = existing
        self.___new = _new
        self.__difference = difference

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get__new(self):
        return self.___new

    def _set__new(self, value):
        if not isinstance(value, list):
            raise TypeError("_new must be list")
        self.___new = value
    _new = property(_get__new, _set__new)

    def _get_difference(self):
        return self.__difference

    def _set_difference(self, value):
        if not isinstance(value, list):
            raise TypeError("difference must be list")
        self.__difference = value
    difference = property(_get_difference, _set_difference)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.___new is not None:
            d['_new'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.___new]
        if self.__difference is not None:
            d['difference'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__difference]
        return d


class ProcessesAndProducts:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class SurfaceWaterDischarge:

    _types_map = {
        'sustainableDrainage': {'type': list, 'subtype': None},
        'soakaway': {'type': list, 'subtype': None},
        'mainSewer': {'type': list, 'subtype': None},
        'existingWatercourse': {'type': list, 'subtype': None},
        'pondLake': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, sustainableDrainage=None, soakaway=None, mainSewer=None, existingWatercourse=None, pondLake=None
                 ):
        self.__sustainableDrainage = sustainableDrainage
        self.__soakaway = soakaway
        self.__mainSewer = mainSewer
        self.__existingWatercourse = existingWatercourse
        self.__pondLake = pondLake

    def _get_sustainableDrainage(self):
        return self.__sustainableDrainage

    def _set_sustainableDrainage(self, value):
        if not isinstance(value, list):
            raise TypeError("sustainableDrainage must be list")
        self.__sustainableDrainage = value
    sustainableDrainage = property(_get_sustainableDrainage, _set_sustainableDrainage)

    def _get_soakaway(self):
        return self.__soakaway

    def _set_soakaway(self, value):
        if not isinstance(value, list):
            raise TypeError("soakaway must be list")
        self.__soakaway = value
    soakaway = property(_get_soakaway, _set_soakaway)

    def _get_mainSewer(self):
        return self.__mainSewer

    def _set_mainSewer(self, value):
        if not isinstance(value, list):
            raise TypeError("mainSewer must be list")
        self.__mainSewer = value
    mainSewer = property(_get_mainSewer, _set_mainSewer)

    def _get_existingWatercourse(self):
        return self.__existingWatercourse

    def _set_existingWatercourse(self, value):
        if not isinstance(value, list):
            raise TypeError("existingWatercourse must be list")
        self.__existingWatercourse = value
    existingWatercourse = property(_get_existingWatercourse, _set_existingWatercourse)

    def _get_pondLake(self):
        return self.__pondLake

    def _set_pondLake(self, value):
        if not isinstance(value, list):
            raise TypeError("pondLake must be list")
        self.__pondLake = value
    pondLake = property(_get_pondLake, _set_pondLake)

    def as_dict(self):
        d = dict()
        if self.__sustainableDrainage is not None:
            d['sustainableDrainage'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__sustainableDrainage]
        if self.__soakaway is not None:
            d['soakaway'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__soakaway]
        if self.__mainSewer is not None:
            d['mainSewer'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__mainSewer]
        if self.__existingWatercourse is not None:
            d['existingWatercourse'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingWatercourse]
        if self.__pondLake is not None:
            d['pondLake'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__pondLake]
        return d


class NoticeGivenDate:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class ExternalAddress:

    _types_map = {
        'internationalAddress': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, internationalAddress=None
                 ):
        self.__internationalAddress = internationalAddress

    def _get_internationalAddress(self):
        return self.__internationalAddress

    def _set_internationalAddress(self, value):
        if not isinstance(value, list):
            raise TypeError("internationalAddress must be list")
        self.__internationalAddress = value
    internationalAddress = property(_get_internationalAddress, _set_internationalAddress)

    def as_dict(self):
        d = dict()
        if self.__internationalAddress is not None:
            d['internationalAddress'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__internationalAddress]
        return d


class D2:

    _types_map = {
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None, monToFri=None, sat=None, sunBH=None
                 ):
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def as_dict(self):
        d = dict()
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        return d


class OtherIncineration:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class B1B:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class ResidentialDevelopment:

    _types_map = {
        'doesIncludeGainOrLoss': {'type': list, 'subtype': None},
        'existing': {'type': list, 'subtype': None},
        'proposed': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, doesIncludeGainOrLoss=None, existing=None, proposed=None
                 ):
        self.__doesIncludeGainOrLoss = doesIncludeGainOrLoss
        self.__existing = existing
        self.__proposed = proposed

    def _get_doesIncludeGainOrLoss(self):
        return self.__doesIncludeGainOrLoss

    def _set_doesIncludeGainOrLoss(self, value):
        if not isinstance(value, list):
            raise TypeError("doesIncludeGainOrLoss must be list")
        self.__doesIncludeGainOrLoss = value
    doesIncludeGainOrLoss = property(_get_doesIncludeGainOrLoss, _set_doesIncludeGainOrLoss)

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get_proposed(self):
        return self.__proposed

    def _set_proposed(self, value):
        if not isinstance(value, list):
            raise TypeError("proposed must be list")
        self.__proposed = value
    proposed = property(_get_proposed, _set_proposed)

    def as_dict(self):
        d = dict()
        if self.__doesIncludeGainOrLoss is not None:
            d['doesIncludeGainOrLoss'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__doesIncludeGainOrLoss]
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.__proposed is not None:
            d['proposed'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__proposed]
        return d


class C3:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        return d


class FileAttachments:

    _types_map = {
        'fileAttachment': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, fileAttachment=None
                 ):
        self.__fileAttachment = fileAttachment

    def _get_fileAttachment(self):
        return self.__fileAttachment

    def _set_fileAttachment(self, value):
        if not isinstance(value, list):
            raise TypeError("fileAttachment must be list")
        self.__fileAttachment = value
    fileAttachment = property(_get_fileAttachment, _set_fileAttachment)

    def as_dict(self):
        d = dict()
        if self.__fileAttachment is not None:
            d['fileAttachment'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__fileAttachment]
        return d


class Telephone:

    _types_map = {
        'telNationalNumber': {'type': list, 'subtype': None},
        'telMobile': {'type': list, 'subtype': None},
        'telPreferred': {'type': list, 'subtype': None},
        'telUse': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, telNationalNumber=None, telMobile=None, telPreferred=None, telUse=None
                 ):
        self.__telNationalNumber = telNationalNumber
        self.__telMobile = telMobile
        self.__telPreferred = telPreferred
        self.__telUse = telUse

    def _get_telNationalNumber(self):
        return self.__telNationalNumber

    def _set_telNationalNumber(self, value):
        if not isinstance(value, list):
            raise TypeError("telNationalNumber must be list")
        self.__telNationalNumber = value
    telNationalNumber = property(_get_telNationalNumber, _set_telNationalNumber)

    def _get_telMobile(self):
        return self.__telMobile

    def _set_telMobile(self, value):
        if not isinstance(value, list):
            raise TypeError("telMobile must be list")
        self.__telMobile = value
    telMobile = property(_get_telMobile, _set_telMobile)

    def _get_telPreferred(self):
        return self.__telPreferred

    def _set_telPreferred(self, value):
        if not isinstance(value, list):
            raise TypeError("telPreferred must be list")
        self.__telPreferred = value
    telPreferred = property(_get_telPreferred, _set_telPreferred)

    def _get_telUse(self):
        return self.__telUse

    def _set_telUse(self, value):
        if not isinstance(value, list):
            raise TypeError("telUse must be list")
        self.__telUse = value
    telUse = property(_get_telUse, _set_telUse)

    def as_dict(self):
        d = dict()
        if self.__telNationalNumber is not None:
            d['telNationalNumber'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__telNationalNumber]
        if self.__telMobile is not None:
            d['telMobile'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__telMobile]
        if self.__telPreferred is not None:
            d['telPreferred'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__telPreferred]
        if self.__telUse is not None:
            d['telUse'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__telUse]
        return d


class Substance:

    _types_map = {
        'substanceName': {'type': list, 'subtype': None},
        'substanceQuantity': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, substanceName=None, substanceQuantity=None
                 ):
        self.__substanceName = substanceName
        self.__substanceQuantity = substanceQuantity

    def _get_substanceName(self):
        return self.__substanceName

    def _set_substanceName(self, value):
        if not isinstance(value, list):
            raise TypeError("substanceName must be list")
        self.__substanceName = value
    substanceName = property(_get_substanceName, _set_substanceName)

    def _get_substanceQuantity(self):
        return self.__substanceQuantity

    def _set_substanceQuantity(self, value):
        if not isinstance(value, list):
            raise TypeError("substanceQuantity must be list")
        self.__substanceQuantity = value
    substanceQuantity = property(_get_substanceQuantity, _set_substanceQuantity)

    def as_dict(self):
        d = dict()
        if self.__substanceName is not None:
            d['substanceName'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__substanceName]
        if self.__substanceQuantity is not None:
            d['substanceQuantity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__substanceQuantity]
        return d


class OwnershipDeclaration:

    _types_map = {
        'declarationDate': {'type': list, 'subtype': None},
        'declarationMade': {'type': list, 'subtype': None},
        'signatory': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, declarationDate=None, declarationMade=None, signatory=None
                 ):
        self.__declarationDate = declarationDate
        self.__declarationMade = declarationMade
        self.__signatory = signatory

    def _get_declarationDate(self):
        return self.__declarationDate

    def _set_declarationDate(self, value):
        if not isinstance(value, list):
            raise TypeError("declarationDate must be list")
        self.__declarationDate = value
    declarationDate = property(_get_declarationDate, _set_declarationDate)

    def _get_declarationMade(self):
        return self.__declarationMade

    def _set_declarationMade(self, value):
        if not isinstance(value, list):
            raise TypeError("declarationMade must be list")
        self.__declarationMade = value
    declarationMade = property(_get_declarationMade, _set_declarationMade)

    def _get_signatory(self):
        return self.__signatory

    def _set_signatory(self, value):
        if not isinstance(value, list):
            raise TypeError("signatory must be list")
        self.__signatory = value
    signatory = property(_get_signatory, _set_signatory)

    def as_dict(self):
        d = dict()
        if self.__declarationDate is not None:
            d['declarationDate'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__declarationDate]
        if self.__declarationMade is not None:
            d['declarationMade'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__declarationMade]
        if self.__signatory is not None:
            d['signatory'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__signatory]
        return d


class Market:

    _types_map = {
        'total': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, total=None
                 ):
        self.__total = total

    def _get_total(self):
        return self.__total

    def _set_total(self, value):
        if not isinstance(value, list):
            raise TypeError("total must be list")
        self.__total = value
    total = property(_get_total, _set_total)

    def as_dict(self):
        d = dict()
        if self.__total is not None:
            d['total'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__total]
        return d


class PersonName:

    _types_map = {
        'personNameTitle': {'type': list, 'subtype': None},
        'personGivenName': {'type': list, 'subtype': None},
        'personFamilyName': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, personNameTitle=None, personGivenName=None, personFamilyName=None
                 ):
        self.__personNameTitle = personNameTitle
        self.__personGivenName = personGivenName
        self.__personFamilyName = personFamilyName

    def _get_personNameTitle(self):
        return self.__personNameTitle

    def _set_personNameTitle(self, value):
        if not isinstance(value, list):
            raise TypeError("personNameTitle must be list")
        self.__personNameTitle = value
    personNameTitle = property(_get_personNameTitle, _set_personNameTitle)

    def _get_personGivenName(self):
        return self.__personGivenName

    def _set_personGivenName(self, value):
        if not isinstance(value, list):
            raise TypeError("personGivenName must be list")
        self.__personGivenName = value
    personGivenName = property(_get_personGivenName, _set_personGivenName)

    def _get_personFamilyName(self):
        return self.__personFamilyName

    def _set_personFamilyName(self, value):
        if not isinstance(value, list):
            raise TypeError("personFamilyName must be list")
        self.__personFamilyName = value
    personFamilyName = property(_get_personFamilyName, _set_personFamilyName)

    def as_dict(self):
        d = dict()
        if self.__personNameTitle is not None:
            d['personNameTitle'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__personNameTitle]
        if self.__personGivenName is not None:
            d['personGivenName'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__personGivenName]
        if self.__personFamilyName is not None:
            d['personFamilyName'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__personFamilyName]
        return d


class SiteVisit:

    _types_map = {
        'seeSite': {'type': list, 'subtype': None},
        'visitContactDetails': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, seeSite=None, visitContactDetails=None
                 ):
        self.__seeSite = seeSite
        self.__visitContactDetails = visitContactDetails

    def _get_seeSite(self):
        return self.__seeSite

    def _set_seeSite(self, value):
        if not isinstance(value, list):
            raise TypeError("seeSite must be list")
        self.__seeSite = value
    seeSite = property(_get_seeSite, _set_seeSite)

    def _get_visitContactDetails(self):
        return self.__visitContactDetails

    def _set_visitContactDetails(self, value):
        if not isinstance(value, list):
            raise TypeError("visitContactDetails must be list")
        self.__visitContactDetails = value
    visitContactDetails = property(_get_visitContactDetails, _set_visitContactDetails)

    def as_dict(self):
        d = dict()
        if self.__seeSite is not None:
            d['seeSite'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__seeSite]
        if self.__visitContactDetails is not None:
            d['visitContactDetails'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__visitContactDetails]
        return d


class ContactOther:

    _types_map = {
        'personName': {'type': list, 'subtype': None},
        'contactDetails': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, personName=None, contactDetails=None
                 ):
        self.__personName = personName
        self.__contactDetails = contactDetails

    def _get_personName(self):
        return self.__personName

    def _set_personName(self, value):
        if not isinstance(value, list):
            raise TypeError("personName must be list")
        self.__personName = value
    personName = property(_get_personName, _set_personName)

    def _get_contactDetails(self):
        return self.__contactDetails

    def _set_contactDetails(self, value):
        if not isinstance(value, list):
            raise TypeError("contactDetails must be list")
        self.__contactDetails = value
    contactDetails = property(_get_contactDetails, _set_contactDetails)

    def as_dict(self):
        d = dict()
        if self.__personName is not None:
            d['personName'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__personName]
        if self.__contactDetails is not None:
            d['contactDetails'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__contactDetails]
        return d


class OtherWasteManagement:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class ContactDetails:

    _types_map = {
        'email': {'type': list, 'subtype': None},
        'telephone': {'type': list, 'subtype': None},
        'fax': {'type': list, 'subtype': None},
        'preferredContactMedium': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, email=None, telephone=None, fax=None, preferredContactMedium=None
                 ):
        self.__email = email
        self.__telephone = telephone
        self.__fax = fax
        self.__preferredContactMedium = preferredContactMedium

    def _get_email(self):
        return self.__email

    def _set_email(self, value):
        if not isinstance(value, list):
            raise TypeError("email must be list")
        self.__email = value
    email = property(_get_email, _set_email)

    def _get_telephone(self):
        return self.__telephone

    def _set_telephone(self, value):
        if not isinstance(value, list):
            raise TypeError("telephone must be list")
        self.__telephone = value
    telephone = property(_get_telephone, _set_telephone)

    def _get_fax(self):
        return self.__fax

    def _set_fax(self, value):
        if not isinstance(value, list):
            raise TypeError("fax must be list")
        self.__fax = value
    fax = property(_get_fax, _set_fax)

    def _get_preferredContactMedium(self):
        return self.__preferredContactMedium

    def _set_preferredContactMedium(self, value):
        if not isinstance(value, list):
            raise TypeError("preferredContactMedium must be list")
        self.__preferredContactMedium = value
    preferredContactMedium = property(_get_preferredContactMedium, _set_preferredContactMedium)

    def as_dict(self):
        d = dict()
        if self.__email is not None:
            d['email'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__email]
        if self.__telephone is not None:
            d['telephone'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__telephone]
        if self.__fax is not None:
            d['fax'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__fax]
        if self.__preferredContactMedium is not None:
            d['preferredContactMedium'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__preferredContactMedium]
        return d


class InvesselComposting:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class OtherTreatment:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class VehicleTotals:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        '_new': {'type': list, 'subtype': None},
        'difference': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, _new=None, difference=None
                 ):
        self.__existing = existing
        self.___new = _new
        self.__difference = difference

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get__new(self):
        return self.___new

    def _set__new(self, value):
        if not isinstance(value, list):
            raise TypeError("_new must be list")
        self.___new = value
    _new = property(_get__new, _set__new)

    def _get_difference(self):
        return self.__difference

    def _set_difference(self, value):
        if not isinstance(value, list):
            raise TypeError("difference must be list")
        self.__difference = value
    difference = property(_get_difference, _set_difference)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.___new is not None:
            d['_new'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.___new]
        if self.__difference is not None:
            d['difference'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__difference]
        return d


class OpenWindrowComposting:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class ConstructingNewBuilding:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class StartTime:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class HazardousSubstances:

    _types_map = {
        'isUseStorageFollowingMaterials': {'type': list, 'subtype': None},
        'substance': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, isUseStorageFollowingMaterials=None, substance=None
                 ):
        self.__isUseStorageFollowingMaterials = isUseStorageFollowingMaterials
        self.__substance = substance

    def _get_isUseStorageFollowingMaterials(self):
        return self.__isUseStorageFollowingMaterials

    def _set_isUseStorageFollowingMaterials(self, value):
        if not isinstance(value, list):
            raise TypeError("isUseStorageFollowingMaterials must be list")
        self.__isUseStorageFollowingMaterials = value
    isUseStorageFollowingMaterials = property(
        _get_isUseStorageFollowingMaterials, _set_isUseStorageFollowingMaterials)

    def _get_substance(self):
        return self.__substance

    def _set_substance(self, value):
        if not isinstance(value, list):
            raise TypeError("substance must be list")
        self.__substance = value
    substance = property(_get_substance, _set_substance)

    def as_dict(self):
        d = dict()
        if self.__isUseStorageFollowingMaterials is not None:
            d['isUseStorageFollowingMaterials'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__isUseStorageFollowingMaterials]
        if self.__substance is not None:
            d['substance'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__substance]
        return d


class TotalVoidCapacity:

    _types_map = {
        'volumeUnit': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, volumeUnit=None
                 ):
        self.__volumeUnit = volumeUnit

    def _get_volumeUnit(self):
        return self.__volumeUnit

    def _set_volumeUnit(self, value):
        if not isinstance(value, list):
            raise TypeError("volumeUnit must be list")
        self.__volumeUnit = value
    volumeUnit = property(_get_volumeUnit, _set_volumeUnit)

    def as_dict(self):
        d = dict()
        if self.__volumeUnit is not None:
            d['volumeUnit'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__volumeUnit]
        return d


class A5:

    _types_map = {
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None, monToFri=None, sat=None, sunBH=None
                 ):
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def as_dict(self):
        d = dict()
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        return d


class A3:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class A2:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class SunBH:

    _types_map = {
        'startTime': {'type': list, 'subtype': None},
        'stopTime': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, startTime=None, stopTime=None
                 ):
        self.__startTime = startTime
        self.__stopTime = stopTime

    def _get_startTime(self):
        return self.__startTime

    def _set_startTime(self, value):
        if not isinstance(value, list):
            raise TypeError("startTime must be list")
        self.__startTime = value
    startTime = property(_get_startTime, _set_startTime)

    def _get_stopTime(self):
        return self.__stopTime

    def _set_stopTime(self, value):
        if not isinstance(value, list):
            raise TypeError("stopTime must be list")
        self.__stopTime = value
    stopTime = property(_get_stopTime, _set_stopTime)

    def as_dict(self):
        d = dict()
        if self.__startTime is not None:
            d['startTime'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__startTime]
        if self.__stopTime is not None:
            d['stopTime'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__stopTime]
        return d


class ConstructionDemolitionExcavation:

    _types_map = {
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, maxAnnualOperationalThroughput=None
                 ):
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class StorageOfWaste:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class AllTreesHedges:

    _types_map = {
        'fullTreesHedges': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, fullTreesHedges=None
                 ):
        self.__fullTreesHedges = fullTreesHedges

    def _get_fullTreesHedges(self):
        return self.__fullTreesHedges

    def _set_fullTreesHedges(self, value):
        if not isinstance(value, list):
            raise TypeError("fullTreesHedges must be list")
        self.__fullTreesHedges = value
    fullTreesHedges = property(_get_fullTreesHedges, _set_fullTreesHedges)

    def as_dict(self):
        d = dict()
        if self.__fullTreesHedges is not None:
            d['fullTreesHedges'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__fullTreesHedges]
        return d


class SubstanceQuantity:

    _types_map = {
        'value': {'type': list, 'subtype': None},
        'volumeUnit': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, value=None, volumeUnit=None
                 ):
        self.__value = value
        self.__volumeUnit = volumeUnit

    def _get_value(self):
        return self.__value

    def _set_value(self, value):
        if not isinstance(value, list):
            raise TypeError("value must be list")
        self.__value = value
    value = property(_get_value, _set_value)

    def _get_volumeUnit(self):
        return self.__volumeUnit

    def _set_volumeUnit(self, value):
        if not isinstance(value, list):
            raise TypeError("volumeUnit must be list")
        self.__volumeUnit = value
    volumeUnit = property(_get_volumeUnit, _set_volumeUnit)

    def as_dict(self):
        d = dict()
        if self.__value is not None:
            d['value'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__value]
        if self.__volumeUnit is not None:
            d['volumeUnit'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__volumeUnit]
        return d


class FullParking:

    _types_map = {
        'cars': {'type': list, 'subtype': None},
        'goodsVehicle': {'type': list, 'subtype': None},
        'motorcycle': {'type': list, 'subtype': None},
        'disability': {'type': list, 'subtype': None},
        'cycle': {'type': list, 'subtype': None},
        'otherVehicle': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, cars=None, goodsVehicle=None, motorcycle=None, disability=None, cycle=None, otherVehicle=None
                 ):
        self.__cars = cars
        self.__goodsVehicle = goodsVehicle
        self.__motorcycle = motorcycle
        self.__disability = disability
        self.__cycle = cycle
        self.__otherVehicle = otherVehicle

    def _get_cars(self):
        return self.__cars

    def _set_cars(self, value):
        if not isinstance(value, list):
            raise TypeError("cars must be list")
        self.__cars = value
    cars = property(_get_cars, _set_cars)

    def _get_goodsVehicle(self):
        return self.__goodsVehicle

    def _set_goodsVehicle(self, value):
        if not isinstance(value, list):
            raise TypeError("goodsVehicle must be list")
        self.__goodsVehicle = value
    goodsVehicle = property(_get_goodsVehicle, _set_goodsVehicle)

    def _get_motorcycle(self):
        return self.__motorcycle

    def _set_motorcycle(self, value):
        if not isinstance(value, list):
            raise TypeError("motorcycle must be list")
        self.__motorcycle = value
    motorcycle = property(_get_motorcycle, _set_motorcycle)

    def _get_disability(self):
        return self.__disability

    def _set_disability(self, value):
        if not isinstance(value, list):
            raise TypeError("disability must be list")
        self.__disability = value
    disability = property(_get_disability, _set_disability)

    def _get_cycle(self):
        return self.__cycle

    def _set_cycle(self, value):
        if not isinstance(value, list):
            raise TypeError("cycle must be list")
        self.__cycle = value
    cycle = property(_get_cycle, _set_cycle)

    def _get_otherVehicle(self):
        return self.__otherVehicle

    def _set_otherVehicle(self, value):
        if not isinstance(value, list):
            raise TypeError("otherVehicle must be list")
        self.__otherVehicle = value
    otherVehicle = property(_get_otherVehicle, _set_otherVehicle)

    def as_dict(self):
        d = dict()
        if self.__cars is not None:
            d['cars'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__cars]
        if self.__goodsVehicle is not None:
            d['goodsVehicle'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__goodsVehicle]
        if self.__motorcycle is not None:
            d['motorcycle'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__motorcycle]
        if self.__disability is not None:
            d['disability'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__disability]
        if self.__cycle is not None:
            d['cycle'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__cycle]
        if self.__otherVehicle is not None:
            d['otherVehicle'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__otherVehicle]
        return d


class Intermediate:

    _types_map = {
        'total': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, total=None
                 ):
        self.__total = total

    def _get_total(self):
        return self.__total

    def _set_total(self, value):
        if not isinstance(value, list):
            raise TypeError("total must be list")
        self.__total = value
    total = property(_get_total, _set_total)

    def as_dict(self):
        d = dict()
        if self.__total is not None:
            d['total'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__total]
        return d


class NoticeGivenTo:

    _types_map = {
        'noticeRecipient': {'type': list, 'subtype': None},
        'noticeGivenDate': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, noticeRecipient=None, noticeGivenDate=None
                 ):
        self.__noticeRecipient = noticeRecipient
        self.__noticeGivenDate = noticeGivenDate

    def _get_noticeRecipient(self):
        return self.__noticeRecipient

    def _set_noticeRecipient(self, value):
        if not isinstance(value, list):
            raise TypeError("noticeRecipient must be list")
        self.__noticeRecipient = value
    noticeRecipient = property(_get_noticeRecipient, _set_noticeRecipient)

    def _get_noticeGivenDate(self):
        return self.__noticeGivenDate

    def _set_noticeGivenDate(self, value):
        if not isinstance(value, list):
            raise TypeError("noticeGivenDate must be list")
        self.__noticeGivenDate = value
    noticeGivenDate = property(_get_noticeGivenDate, _set_noticeGivenDate)

    def as_dict(self):
        d = dict()
        if self.__noticeRecipient is not None:
            d['noticeRecipient'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__noticeRecipient]
        if self.__noticeGivenDate is not None:
            d['noticeGivenDate'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__noticeGivenDate]
        return d


class AnaerobicDigestion:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class Fax:

    _types_map = {
        'faxNationalNumber': {'type': list, 'subtype': None},
        'faxMobile': {'type': list, 'subtype': None},
        'faxPreferred': {'type': list, 'subtype': None},
        'faxUse': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, faxNationalNumber=None, faxMobile=None, faxPreferred=None, faxUse=None
                 ):
        self.__faxNationalNumber = faxNationalNumber
        self.__faxMobile = faxMobile
        self.__faxPreferred = faxPreferred
        self.__faxUse = faxUse

    def _get_faxNationalNumber(self):
        return self.__faxNationalNumber

    def _set_faxNationalNumber(self, value):
        if not isinstance(value, list):
            raise TypeError("faxNationalNumber must be list")
        self.__faxNationalNumber = value
    faxNationalNumber = property(_get_faxNationalNumber, _set_faxNationalNumber)

    def _get_faxMobile(self):
        return self.__faxMobile

    def _set_faxMobile(self, value):
        if not isinstance(value, list):
            raise TypeError("faxMobile must be list")
        self.__faxMobile = value
    faxMobile = property(_get_faxMobile, _set_faxMobile)

    def _get_faxPreferred(self):
        return self.__faxPreferred

    def _set_faxPreferred(self, value):
        if not isinstance(value, list):
            raise TypeError("faxPreferred must be list")
        self.__faxPreferred = value
    faxPreferred = property(_get_faxPreferred, _set_faxPreferred)

    def _get_faxUse(self):
        return self.__faxUse

    def _set_faxUse(self, value):
        if not isinstance(value, list):
            raise TypeError("faxUse must be list")
        self.__faxUse = value
    faxUse = property(_get_faxUse, _set_faxUse)

    def as_dict(self):
        d = dict()
        if self.__faxNationalNumber is not None:
            d['faxNationalNumber'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__faxNationalNumber]
        if self.__faxMobile is not None:
            d['faxMobile'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__faxMobile]
        if self.__faxPreferred is not None:
            d['faxPreferred'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__faxPreferred]
        if self.__faxUse is not None:
            d['faxUse'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__faxUse]
        return d


class Applicant:

    _types_map = {
        'personName': {'type': list, 'subtype': None},
        'externalAddress': {'type': list, 'subtype': None},
        'contactDetails': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, personName=None, externalAddress=None, contactDetails=None
                 ):
        self.__personName = personName
        self.__externalAddress = externalAddress
        self.__contactDetails = contactDetails

    def _get_personName(self):
        return self.__personName

    def _set_personName(self, value):
        if not isinstance(value, list):
            raise TypeError("personName must be list")
        self.__personName = value
    personName = property(_get_personName, _set_personName)

    def _get_externalAddress(self):
        return self.__externalAddress

    def _set_externalAddress(self, value):
        if not isinstance(value, list):
            raise TypeError("externalAddress must be list")
        self.__externalAddress = value
    externalAddress = property(_get_externalAddress, _set_externalAddress)

    def _get_contactDetails(self):
        return self.__contactDetails

    def _set_contactDetails(self, value):
        if not isinstance(value, list):
            raise TypeError("contactDetails must be list")
        self.__contactDetails = value
    contactDetails = property(_get_contactDetails, _set_contactDetails)

    def as_dict(self):
        d = dict()
        if self.__personName is not None:
            d['personName'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__personName]
        if self.__externalAddress is not None:
            d['externalAddress'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__externalAddress]
        if self.__contactDetails is not None:
            d['contactDetails'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__contactDetails]
        return d


class ProposalState:

    _types_map = {
        'proposalStarted': {'type': list, 'subtype': None},
        'proposalCompleted': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, proposalStarted=None, proposalCompleted=None
                 ):
        self.__proposalStarted = proposalStarted
        self.__proposalCompleted = proposalCompleted

    def _get_proposalStarted(self):
        return self.__proposalStarted

    def _set_proposalStarted(self, value):
        if not isinstance(value, list):
            raise TypeError("proposalStarted must be list")
        self.__proposalStarted = value
    proposalStarted = property(_get_proposalStarted, _set_proposalStarted)

    def _get_proposalCompleted(self):
        return self.__proposalCompleted

    def _set_proposalCompleted(self, value):
        if not isinstance(value, list):
            raise TypeError("proposalCompleted must be list")
        self.__proposalCompleted = value
    proposalCompleted = property(_get_proposalCompleted, _set_proposalCompleted)

    def as_dict(self):
        d = dict()
        if self.__proposalStarted is not None:
            d['proposalStarted'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__proposalStarted]
        if self.__proposalCompleted is not None:
            d['proposalCompleted'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__proposalCompleted]
        return d


class BS7666Address:

    _types_map = {
        'paon': {'type': list, 'subtype': None},
        'streetDescription': {'type': list, 'subtype': None},
        'locality': {'type': list, 'subtype': None},
        'town': {'type': list, 'subtype': None},
        'postTown': {'type': list, 'subtype': None},
        'postCode': {'type': list, 'subtype': None},
        'uniquePropertyReferenceNumber': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, paon=None, streetDescription=None, locality=None, town=None, postTown=None, postCode=None, uniquePropertyReferenceNumber=None
                 ):
        self.__paon = paon
        self.__streetDescription = streetDescription
        self.__locality = locality
        self.__town = town
        self.__postTown = postTown
        self.__postCode = postCode
        self.__uniquePropertyReferenceNumber = uniquePropertyReferenceNumber

    def _get_paon(self):
        return self.__paon

    def _set_paon(self, value):
        if not isinstance(value, list):
            raise TypeError("paon must be list")
        self.__paon = value
    paon = property(_get_paon, _set_paon)

    def _get_streetDescription(self):
        return self.__streetDescription

    def _set_streetDescription(self, value):
        if not isinstance(value, list):
            raise TypeError("streetDescription must be list")
        self.__streetDescription = value
    streetDescription = property(_get_streetDescription, _set_streetDescription)

    def _get_locality(self):
        return self.__locality

    def _set_locality(self, value):
        if not isinstance(value, list):
            raise TypeError("locality must be list")
        self.__locality = value
    locality = property(_get_locality, _set_locality)

    def _get_town(self):
        return self.__town

    def _set_town(self, value):
        if not isinstance(value, list):
            raise TypeError("town must be list")
        self.__town = value
    town = property(_get_town, _set_town)

    def _get_postTown(self):
        return self.__postTown

    def _set_postTown(self, value):
        if not isinstance(value, list):
            raise TypeError("postTown must be list")
        self.__postTown = value
    postTown = property(_get_postTown, _set_postTown)

    def _get_postCode(self):
        return self.__postCode

    def _set_postCode(self, value):
        if not isinstance(value, list):
            raise TypeError("postCode must be list")
        self.__postCode = value
    postCode = property(_get_postCode, _set_postCode)

    def _get_uniquePropertyReferenceNumber(self):
        return self.__uniquePropertyReferenceNumber

    def _set_uniquePropertyReferenceNumber(self, value):
        if not isinstance(value, list):
            raise TypeError("uniquePropertyReferenceNumber must be list")
        self.__uniquePropertyReferenceNumber = value
    uniquePropertyReferenceNumber = property(
        _get_uniquePropertyReferenceNumber, _set_uniquePropertyReferenceNumber)

    def as_dict(self):
        d = dict()
        if self.__paon is not None:
            d['paon'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__paon]
        if self.__streetDescription is not None:
            d['streetDescription'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__streetDescription]
        if self.__locality is not None:
            d['locality'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__locality]
        if self.__town is not None:
            d['town'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__town]
        if self.__postTown is not None:
            d['postTown'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__postTown]
        if self.__postCode is not None:
            d['postCode'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__postCode]
        if self.__uniquePropertyReferenceNumber is not None:
            d['uniquePropertyReferenceNumber'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__uniquePropertyReferenceNumber]
        return d


class IndustrialCommercial:

    _types_map = {
        'isProposalWasteManagementDevelopment': {'type': list, 'subtype': None},
        'processesAndProducts': {'type': list, 'subtype': None},
        'wasteManagementDetails': {'type': list, 'subtype': None},
        'wasteStreamDetails': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, isProposalWasteManagementDevelopment=None, processesAndProducts=None, wasteManagementDetails=None, wasteStreamDetails=None
                 ):
        self.__isProposalWasteManagementDevelopment = isProposalWasteManagementDevelopment
        self.__processesAndProducts = processesAndProducts
        self.__wasteManagementDetails = wasteManagementDetails
        self.__wasteStreamDetails = wasteStreamDetails

    def _get_isProposalWasteManagementDevelopment(self):
        return self.__isProposalWasteManagementDevelopment

    def _set_isProposalWasteManagementDevelopment(self, value):
        if not isinstance(value, list):
            raise TypeError("isProposalWasteManagementDevelopment must be list")
        self.__isProposalWasteManagementDevelopment = value
    isProposalWasteManagementDevelopment = property(
        _get_isProposalWasteManagementDevelopment, _set_isProposalWasteManagementDevelopment)

    def _get_processesAndProducts(self):
        return self.__processesAndProducts

    def _set_processesAndProducts(self, value):
        if not isinstance(value, list):
            raise TypeError("processesAndProducts must be list")
        self.__processesAndProducts = value
    processesAndProducts = property(_get_processesAndProducts, _set_processesAndProducts)

    def _get_wasteManagementDetails(self):
        return self.__wasteManagementDetails

    def _set_wasteManagementDetails(self, value):
        if not isinstance(value, list):
            raise TypeError("wasteManagementDetails must be list")
        self.__wasteManagementDetails = value
    wasteManagementDetails = property(_get_wasteManagementDetails, _set_wasteManagementDetails)

    def _get_wasteStreamDetails(self):
        return self.__wasteStreamDetails

    def _set_wasteStreamDetails(self, value):
        if not isinstance(value, list):
            raise TypeError("wasteStreamDetails must be list")
        self.__wasteStreamDetails = value
    wasteStreamDetails = property(_get_wasteStreamDetails, _set_wasteStreamDetails)

    def as_dict(self):
        d = dict()
        if self.__isProposalWasteManagementDevelopment is not None:
            d['isProposalWasteManagementDevelopment'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__isProposalWasteManagementDevelopment]
        if self.__processesAndProducts is not None:
            d['processesAndProducts'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__processesAndProducts]
        if self.__wasteManagementDetails is not None:
            d['wasteManagementDetails'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__wasteManagementDetails]
        if self.__wasteStreamDetails is not None:
            d['wasteStreamDetails'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__wasteStreamDetails]
        return d


class DontKnow:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class StartRange:

    _types_map = {
        'number': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, number=None
                 ):
        self.__number = number

    def _get_number(self):
        return self.__number

    def _set_number(self, value):
        if not isinstance(value, list):
            raise TypeError("number must be list")
        self.__number = value
    number = property(_get_number, _set_number)

    def as_dict(self):
        d = dict()
        if self.__number is not None:
            d['number'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__number]
        return d


class D1:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class FullDate:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class MBTTreatment:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class SiteGridRefence:

    _types_map = {
        'x': {'type': list, 'subtype': None},
        'y': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, x=None, y=None
                 ):
        self.__x = x
        self.__y = y

    def _get_x(self):
        return self.__x

    def _set_x(self, value):
        if not isinstance(value, list):
            raise TypeError("x must be list")
        self.__x = value
    x = property(_get_x, _set_x)

    def _get_y(self):
        return self.__y

    def _set_y(self, value):
        if not isinstance(value, list):
            raise TypeError("y must be list")
        self.__y = value
    y = property(_get_y, _set_y)

    def as_dict(self):
        d = dict()
        if self.__x is not None:
            d['x'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__x]
        if self.__y is not None:
            d['y'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__y]
        return d


class A1:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class MetalRecyclingSite:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class MaterialRecoveryFacilities:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class B8:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class MonToFri:

    _types_map = {
        'startTime': {'type': list, 'subtype': None},
        'stopTime': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, startTime=None, stopTime=None
                 ):
        self.__startTime = startTime
        self.__stopTime = stopTime

    def _get_startTime(self):
        return self.__startTime

    def _set_startTime(self, value):
        if not isinstance(value, list):
            raise TypeError("startTime must be list")
        self.__startTime = value
    startTime = property(_get_startTime, _set_startTime)

    def _get_stopTime(self):
        return self.__stopTime

    def _set_stopTime(self, value):
        if not isinstance(value, list):
            raise TypeError("stopTime must be list")
        self.__stopTime = value
    stopTime = property(_get_stopTime, _set_stopTime)

    def as_dict(self):
        d = dict()
        if self.__startTime is not None:
            d['startTime'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__startTime]
        if self.__stopTime is not None:
            d['stopTime'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__stopTime]
        return d


class Windows:

    _types_map = {
        'notApplicable': {'type': list, 'subtype': None},
        'dontKnow': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, notApplicable=None, dontKnow=None
                 ):
        self.__notApplicable = notApplicable
        self.__dontKnow = dontKnow

    def _get_notApplicable(self):
        return self.__notApplicable

    def _set_notApplicable(self, value):
        if not isinstance(value, list):
            raise TypeError("notApplicable must be list")
        self.__notApplicable = value
    notApplicable = property(_get_notApplicable, _set_notApplicable)

    def _get_dontKnow(self):
        return self.__dontKnow

    def _set_dontKnow(self, value):
        if not isinstance(value, list):
            raise TypeError("dontKnow must be list")
        self.__dontKnow = value
    dontKnow = property(_get_dontKnow, _set_dontKnow)

    def as_dict(self):
        d = dict()
        if self.__notApplicable is not None:
            d['notApplicable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__notApplicable]
        if self.__dontKnow is not None:
            d['dontKnow'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dontKnow]
        return d


class Cycle:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        '_new': {'type': list, 'subtype': None},
        'difference': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, _new=None, difference=None
                 ):
        self.__existing = existing
        self.___new = _new
        self.__difference = difference

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get__new(self):
        return self.___new

    def _set__new(self, value):
        if not isinstance(value, list):
            raise TypeError("_new must be list")
        self.___new = value
    _new = property(_get__new, _set__new)

    def _get_difference(self):
        return self.__difference

    def _set_difference(self, value):
        if not isinstance(value, list):
            raise TypeError("difference must be list")
        self.__difference = value
    difference = property(_get_difference, _set_difference)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.___new is not None:
            d['_new'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.___new]
        if self.__difference is not None:
            d['difference'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__difference]
        return d


class LastUseDescription:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class Advice:

    _types_map = {
        'haveSoughtAdvice': {'type': list, 'subtype': None},
        'adviceDetails': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, haveSoughtAdvice=None, adviceDetails=None
                 ):
        self.__haveSoughtAdvice = haveSoughtAdvice
        self.__adviceDetails = adviceDetails

    def _get_haveSoughtAdvice(self):
        return self.__haveSoughtAdvice

    def _set_haveSoughtAdvice(self, value):
        if not isinstance(value, list):
            raise TypeError("haveSoughtAdvice must be list")
        self.__haveSoughtAdvice = value
    haveSoughtAdvice = property(_get_haveSoughtAdvice, _set_haveSoughtAdvice)

    def _get_adviceDetails(self):
        return self.__adviceDetails

    def _set_adviceDetails(self, value):
        if not isinstance(value, list):
            raise TypeError("adviceDetails must be list")
        self.__adviceDetails = value
    adviceDetails = property(_get_adviceDetails, _set_adviceDetails)

    def as_dict(self):
        d = dict()
        if self.__haveSoughtAdvice is not None:
            d['haveSoughtAdvice'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__haveSoughtAdvice]
        if self.__adviceDetails is not None:
            d['adviceDetails'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__adviceDetails]
        return d


class Municipal:

    _types_map = {
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, maxAnnualOperationalThroughput=None
                 ):
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class Existing:

    _types_map = {
        'content': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, content=None
                 ):
        self.__content = content

    def _get_content(self):
        return self.__content

    def _set_content(self, value):
        if not isinstance(value, list):
            raise TypeError("content must be list")
        self.__content = value
    content = property(_get_content, _set_content)

    def as_dict(self):
        d = dict()
        if self.__content is not None:
            d['content'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__content]
        return d


class B2:

    _types_map = {
        'monToFri': {'type': list, 'subtype': None},
        'sat': {'type': list, 'subtype': None},
        'sunBH': {'type': list, 'subtype': None},
        'existingGrossFloorspace': {'type': list, 'subtype': None},
        'grossFloorspaceToBeLost': {'type': list, 'subtype': None},
        'totalGrossFloorspaceProposed': {'type': list, 'subtype': None},
        'netAdditionalGrossFloorspace': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, monToFri=None, sat=None, sunBH=None, existingGrossFloorspace=None, grossFloorspaceToBeLost=None, totalGrossFloorspaceProposed=None, netAdditionalGrossFloorspace=None
                 ):
        self.__monToFri = monToFri
        self.__sat = sat
        self.__sunBH = sunBH
        self.__existingGrossFloorspace = existingGrossFloorspace
        self.__grossFloorspaceToBeLost = grossFloorspaceToBeLost
        self.__totalGrossFloorspaceProposed = totalGrossFloorspaceProposed
        self.__netAdditionalGrossFloorspace = netAdditionalGrossFloorspace

    def _get_monToFri(self):
        return self.__monToFri

    def _set_monToFri(self, value):
        if not isinstance(value, list):
            raise TypeError("monToFri must be list")
        self.__monToFri = value
    monToFri = property(_get_monToFri, _set_monToFri)

    def _get_sat(self):
        return self.__sat

    def _set_sat(self, value):
        if not isinstance(value, list):
            raise TypeError("sat must be list")
        self.__sat = value
    sat = property(_get_sat, _set_sat)

    def _get_sunBH(self):
        return self.__sunBH

    def _set_sunBH(self, value):
        if not isinstance(value, list):
            raise TypeError("sunBH must be list")
        self.__sunBH = value
    sunBH = property(_get_sunBH, _set_sunBH)

    def _get_existingGrossFloorspace(self):
        return self.__existingGrossFloorspace

    def _set_existingGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("existingGrossFloorspace must be list")
        self.__existingGrossFloorspace = value
    existingGrossFloorspace = property(_get_existingGrossFloorspace, _set_existingGrossFloorspace)

    def _get_grossFloorspaceToBeLost(self):
        return self.__grossFloorspaceToBeLost

    def _set_grossFloorspaceToBeLost(self, value):
        if not isinstance(value, list):
            raise TypeError("grossFloorspaceToBeLost must be list")
        self.__grossFloorspaceToBeLost = value
    grossFloorspaceToBeLost = property(_get_grossFloorspaceToBeLost, _set_grossFloorspaceToBeLost)

    def _get_totalGrossFloorspaceProposed(self):
        return self.__totalGrossFloorspaceProposed

    def _set_totalGrossFloorspaceProposed(self, value):
        if not isinstance(value, list):
            raise TypeError("totalGrossFloorspaceProposed must be list")
        self.__totalGrossFloorspaceProposed = value
    totalGrossFloorspaceProposed = property(
        _get_totalGrossFloorspaceProposed, _set_totalGrossFloorspaceProposed)

    def _get_netAdditionalGrossFloorspace(self):
        return self.__netAdditionalGrossFloorspace

    def _set_netAdditionalGrossFloorspace(self, value):
        if not isinstance(value, list):
            raise TypeError("netAdditionalGrossFloorspace must be list")
        self.__netAdditionalGrossFloorspace = value
    netAdditionalGrossFloorspace = property(
        _get_netAdditionalGrossFloorspace, _set_netAdditionalGrossFloorspace)

    def as_dict(self):
        d = dict()
        if self.__monToFri is not None:
            d['monToFri'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__monToFri]
        if self.__sat is not None:
            d['sat'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sat]
        if self.__sunBH is not None:
            d['sunBH'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__sunBH]
        if self.__existingGrossFloorspace is not None:
            d['existingGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__existingGrossFloorspace]
        if self.__grossFloorspaceToBeLost is not None:
            d['grossFloorspaceToBeLost'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__grossFloorspaceToBeLost]
        if self.__totalGrossFloorspaceProposed is not None:
            d['totalGrossFloorspaceProposed'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalGrossFloorspaceProposed]
        if self.__netAdditionalGrossFloorspace is not None:
            d['netAdditionalGrossFloorspace'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__netAdditionalGrossFloorspace]
        return d


class LastUseEndDate:

    _types_map = {
        'fullDate': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, fullDate=None
                 ):
        self.__fullDate = fullDate

    def _get_fullDate(self):
        return self.__fullDate

    def _set_fullDate(self, value):
        if not isinstance(value, list):
            raise TypeError("fullDate must be list")
        self.__fullDate = value
    fullDate = property(_get_fullDate, _set_fullDate)

    def as_dict(self):
        d = dict()
        if self.__fullDate is not None:
            d['fullDate'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__fullDate]
        return d


class PyrolysisGasification:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class GoodsVehicle:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        '_new': {'type': list, 'subtype': None},
        'difference': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, _new=None, difference=None
                 ):
        self.__existing = existing
        self.___new = _new
        self.__difference = difference

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get__new(self):
        return self.___new

    def _set__new(self, value):
        if not isinstance(value, list):
            raise TypeError("_new must be list")
        self.___new = value
    _new = property(_get__new, _set__new)

    def _get_difference(self):
        return self.__difference

    def _set_difference(self, value):
        if not isinstance(value, list):
            raise TypeError("difference must be list")
        self.__difference = value
    difference = property(_get_difference, _set_difference)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.___new is not None:
            d['_new'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.___new]
        if self.__difference is not None:
            d['difference'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__difference]
        return d


class ApplicationScenario:

    _types_map = {
        'scenarioNumber': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, scenarioNumber=None
                 ):
        self.__scenarioNumber = scenarioNumber

    def _get_scenarioNumber(self):
        return self.__scenarioNumber

    def _set_scenarioNumber(self, value):
        if not isinstance(value, list):
            raise TypeError("scenarioNumber must be list")
        self.__scenarioNumber = value
    scenarioNumber = property(_get_scenarioNumber, _set_scenarioNumber)

    def as_dict(self):
        d = dict()
        if self.__scenarioNumber is not None:
            d['scenarioNumber'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__scenarioNumber]
        return d


class HouseholdCivicAmenitySites:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class ProposalDescription:

    _types_map = {
        'descriptionText': {'type': list, 'subtype': None},
        'proposalState': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, descriptionText=None, proposalState=None
                 ):
        self.__descriptionText = descriptionText
        self.__proposalState = proposalState

    def _get_descriptionText(self):
        return self.__descriptionText

    def _set_descriptionText(self, value):
        if not isinstance(value, list):
            raise TypeError("descriptionText must be list")
        self.__descriptionText = value
    descriptionText = property(_get_descriptionText, _set_descriptionText)

    def _get_proposalState(self):
        return self.__proposalState

    def _set_proposalState(self, value):
        if not isinstance(value, list):
            raise TypeError("proposalState must be list")
        self.__proposalState = value
    proposalState = property(_get_proposalState, _set_proposalState)

    def as_dict(self):
        d = dict()
        if self.__descriptionText is not None:
            d['descriptionText'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__descriptionText]
        if self.__proposalState is not None:
            d['proposalState'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__proposalState]
        return d


class OtherDevelopments:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class AdvertDate:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class Lighting:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        'proposed': {'type': list, 'subtype': None},
        'notApplicable': {'type': list, 'subtype': None},
        'dontKnow': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, proposed=None, notApplicable=None, dontKnow=None
                 ):
        self.__existing = existing
        self.__proposed = proposed
        self.__notApplicable = notApplicable
        self.__dontKnow = dontKnow

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get_proposed(self):
        return self.__proposed

    def _set_proposed(self, value):
        if not isinstance(value, list):
            raise TypeError("proposed must be list")
        self.__proposed = value
    proposed = property(_get_proposed, _set_proposed)

    def _get_notApplicable(self):
        return self.__notApplicable

    def _set_notApplicable(self, value):
        if not isinstance(value, list):
            raise TypeError("notApplicable must be list")
        self.__notApplicable = value
    notApplicable = property(_get_notApplicable, _set_notApplicable)

    def _get_dontKnow(self):
        return self.__dontKnow

    def _set_dontKnow(self, value):
        if not isinstance(value, list):
            raise TypeError("dontKnow must be list")
        self.__dontKnow = value
    dontKnow = property(_get_dontKnow, _set_dontKnow)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.__proposed is not None:
            d['proposed'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__proposed]
        if self.__notApplicable is not None:
            d['notApplicable'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__notApplicable]
        if self.__dontKnow is not None:
            d['dontKnow'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__dontKnow]
        return d


class PAON:

    _types_map = {
        'startRange': {'type': list, 'subtype': None},
        'endRange': {'type': list, 'subtype': None},
        'description': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, startRange=None, endRange=None, description=None
                 ):
        self.__startRange = startRange
        self.__endRange = endRange
        self.__description = description

    def _get_startRange(self):
        return self.__startRange

    def _set_startRange(self, value):
        if not isinstance(value, list):
            raise TypeError("startRange must be list")
        self.__startRange = value
    startRange = property(_get_startRange, _set_startRange)

    def _get_endRange(self):
        return self.__endRange

    def _set_endRange(self, value):
        if not isinstance(value, list):
            raise TypeError("endRange must be list")
        self.__endRange = value
    endRange = property(_get_endRange, _set_endRange)

    def _get_description(self):
        return self.__description

    def _set_description(self, value):
        if not isinstance(value, list):
            raise TypeError("description must be list")
        self.__description = value
    description = property(_get_description, _set_description)

    def as_dict(self):
        d = dict()
        if self.__startRange is not None:
            d['startRange'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__startRange]
        if self.__endRange is not None:
            d['endRange'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__endRange]
        if self.__description is not None:
            d['description'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__description]
        return d


class WasteIncinerationEnergy:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class WasteStreamDetails:

    _types_map = {
        'municipal': {'type': list, 'subtype': None},
        'constructionDemolitionExcavation': {'type': list, 'subtype': None},
        'commercialIndustrial': {'type': list, 'subtype': None},
        'hazardous': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, municipal=None, constructionDemolitionExcavation=None, commercialIndustrial=None, hazardous=None
                 ):
        self.__municipal = municipal
        self.__constructionDemolitionExcavation = constructionDemolitionExcavation
        self.__commercialIndustrial = commercialIndustrial
        self.__hazardous = hazardous

    def _get_municipal(self):
        return self.__municipal

    def _set_municipal(self, value):
        if not isinstance(value, list):
            raise TypeError("municipal must be list")
        self.__municipal = value
    municipal = property(_get_municipal, _set_municipal)

    def _get_constructionDemolitionExcavation(self):
        return self.__constructionDemolitionExcavation

    def _set_constructionDemolitionExcavation(self, value):
        if not isinstance(value, list):
            raise TypeError("constructionDemolitionExcavation must be list")
        self.__constructionDemolitionExcavation = value
    constructionDemolitionExcavation = property(
        _get_constructionDemolitionExcavation, _set_constructionDemolitionExcavation)

    def _get_commercialIndustrial(self):
        return self.__commercialIndustrial

    def _set_commercialIndustrial(self, value):
        if not isinstance(value, list):
            raise TypeError("commercialIndustrial must be list")
        self.__commercialIndustrial = value
    commercialIndustrial = property(_get_commercialIndustrial, _set_commercialIndustrial)

    def _get_hazardous(self):
        return self.__hazardous

    def _set_hazardous(self, value):
        if not isinstance(value, list):
            raise TypeError("hazardous must be list")
        self.__hazardous = value
    hazardous = property(_get_hazardous, _set_hazardous)

    def as_dict(self):
        d = dict()
        if self.__municipal is not None:
            d['municipal'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__municipal]
        if self.__constructionDemolitionExcavation is not None:
            d['constructionDemolitionExcavation'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__constructionDemolitionExcavation]
        if self.__commercialIndustrial is not None:
            d['commercialIndustrial'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__commercialIndustrial]
        if self.__hazardous is not None:
            d['hazardous'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__hazardous]
        return d


class Employment:

    _types_map = {
        'existing': {'type': list, 'subtype': None},
        'proposed': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, existing=None, proposed=None
                 ):
        self.__existing = existing
        self.__proposed = proposed

    def _get_existing(self):
        return self.__existing

    def _set_existing(self, value):
        if not isinstance(value, list):
            raise TypeError("existing must be list")
        self.__existing = value
    existing = property(_get_existing, _set_existing)

    def _get_proposed(self):
        return self.__proposed

    def _set_proposed(self, value):
        if not isinstance(value, list):
            raise TypeError("proposed must be list")
        self.__proposed = value
    proposed = property(_get_proposed, _set_proposed)

    def as_dict(self):
        d = dict()
        if self.__existing is not None:
            d['existing'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__existing]
        if self.__proposed is not None:
            d['proposed'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__proposed]
        return d


class RecyclingFacilitiesCDEWaste:

    _types_map = {
        'totalVoidCapacity': {'type': list, 'subtype': None},
        'maxAnnualOperationalThroughput': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, totalVoidCapacity=None, maxAnnualOperationalThroughput=None
                 ):
        self.__totalVoidCapacity = totalVoidCapacity
        self.__maxAnnualOperationalThroughput = maxAnnualOperationalThroughput

    def _get_totalVoidCapacity(self):
        return self.__totalVoidCapacity

    def _set_totalVoidCapacity(self, value):
        if not isinstance(value, list):
            raise TypeError("totalVoidCapacity must be list")
        self.__totalVoidCapacity = value
    totalVoidCapacity = property(_get_totalVoidCapacity, _set_totalVoidCapacity)

    def _get_maxAnnualOperationalThroughput(self):
        return self.__maxAnnualOperationalThroughput

    def _set_maxAnnualOperationalThroughput(self, value):
        if not isinstance(value, list):
            raise TypeError("maxAnnualOperationalThroughput must be list")
        self.__maxAnnualOperationalThroughput = value
    maxAnnualOperationalThroughput = property(
        _get_maxAnnualOperationalThroughput, _set_maxAnnualOperationalThroughput)

    def as_dict(self):
        d = dict()
        if self.__totalVoidCapacity is not None:
            d['totalVoidCapacity'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__totalVoidCapacity]
        if self.__maxAnnualOperationalThroughput is not None:
            d['maxAnnualOperationalThroughput'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__maxAnnualOperationalThroughput]
        return d


class NotApplicable:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d


class NoticeRecipient:

    _types_map = {
        'noticeRecipientPerson': {'type': list, 'subtype': None},
        'noticeRecipientAddress': {'type': list, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self, noticeRecipientPerson=None, noticeRecipientAddress=None
                 ):
        self.__noticeRecipientPerson = noticeRecipientPerson
        self.__noticeRecipientAddress = noticeRecipientAddress

    def _get_noticeRecipientPerson(self):
        return self.__noticeRecipientPerson

    def _set_noticeRecipientPerson(self, value):
        if not isinstance(value, list):
            raise TypeError("noticeRecipientPerson must be list")
        self.__noticeRecipientPerson = value
    noticeRecipientPerson = property(_get_noticeRecipientPerson, _set_noticeRecipientPerson)

    def _get_noticeRecipientAddress(self):
        return self.__noticeRecipientAddress

    def _set_noticeRecipientAddress(self, value):
        if not isinstance(value, list):
            raise TypeError("noticeRecipientAddress must be list")
        self.__noticeRecipientAddress = value
    noticeRecipientAddress = property(_get_noticeRecipientAddress, _set_noticeRecipientAddress)

    def as_dict(self):
        d = dict()
        if self.__noticeRecipientPerson is not None:
            d['noticeRecipientPerson'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__noticeRecipientPerson]
        if self.__noticeRecipientAddress is not None:
            d['noticeRecipientAddress'] = [p.as_dict() if hasattr(
                p, 'as_dict') else p for p in self.__noticeRecipientAddress]
        return d


class RootObject:

    _types_map = {
    }
    _formats_map = {
    }

    def __init__(self
                 ):

    def as_dict(self):
        d = dict()
        return d

