---
Description: The CarrierControlSignatureSchema schema defines elements that are used to describe the signature appended to the provisioning file.
Search.Product: eADQiWindows 10XVcnh
title: CarrierControlSignatureSchema schema
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c

keywords: windows 10, uwp, schema, mobile broadband schema


ms.topic: reference
ms.date: 04/05/2017
---

# CarrierControlSignatureSchema schema


The CarrierControlSignatureSchema schema defines elements that are used to describe the signature appended to the provisioning file. It is based on the [XML DSIG](https://www.w3.org/TR/xmldsig-core/) specification with only minor deviations that are explicitly described below. All of the elements are in the namespace http://www.w3.org/2000/09/xmldsig\#. Not all elements are in every profile, as some elements are optional.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="element-canonicalizationmethod.md">CanonicalizationMethod</a> </td>
<td><p>Defines the canonicalization method applied to <a href="element-signedinfo.md"><strong>SignedInfo</strong></a>  as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>. Must be of type Canonical XML.</p></td>
</tr>
<tr class="even">
<td><a href="element-dsakeyvalue.md">DSAKeyValue</a> </td>
<td><p>Defines a Digital Signature Algorithm (DSA) public key as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="odd">
<td><a href="element-digestmethod.md">DigestMethod</a> </td>
<td><p>Defines the algorithm used to generate <a href="element-digestvalue.md"><strong>DigestValue</strong></a>  as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="even">
<td><a href="element-digestvalue.md">DigestValue</a> </td>
<td><p>Defines the digest value as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> . The algorithm used to generate <a href="element-digestvalue.md"><strong>DigestValue</strong></a> is defined in <a href="element-digestmethod.md"><strong>DigestMethod</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-exponent.md">Exponent</a> </td>
<td><p>Defines the RSA public key exponent as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-g.md">G</a> </td>
<td><p>Defines an integer with certain properties with respect to <a href="element-p.md"><strong>P</strong></a>  and <a href="element-q.md"><strong>Q</strong></a> as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-hmacoutputlength.md">HMACOutputLength</a> </td>
<td><p>Defines the length, in bits, of the <a href="element-signaturevalue.md"><strong>SignatureValue</strong></a>  element as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="even">
<td><a href="element-j.md">J</a> </td>
<td><p>Defines (<a href="element-p.md"><strong>P</strong></a>  - 1) / <a href="element-q.md"><strong>Q</strong></a> as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-keyinfo.md">KeyInfo</a> </td>
<td><p>Defines all key information used to validate the signature as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-keyvalue.md">KeyValue</a> </td>
<td><p>Defines a single public key as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="odd">
<td><a href="element-modulus.md">Modulus</a> </td>
<td><p>Defines the RSA public key modulus as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-p.md">P</a> </td>
<td><p>Defines a prime modulus meeting the <a href="https://www.w3.org/2000/09/xmldsig#dsa-sha1 ">DSAwithSHA1</a>  requirements as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-pgencounter.md">PgenCounter</a> </td>
<td><p>Defines a Digital Signature Algorithm (DSA) prime generation counter as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-q.md">Q</a> </td>
<td><p>Defines an integer in the range 2**159 &lt; <a href="element-q.md"><strong>Q</strong></a>  &lt; 2**160 which is a prime divisor of <a href="element-p.md"><strong>P</strong></a>-1 as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-rsakeyvalue.md">RSAKeyValue</a> </td>
<td><p>Defines a RSA public key as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-reference.md">Reference</a> </td>
<td><p>Defines a digest value, digest method, and transforms as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="odd">
<td><a href="element-seed.md">Seed</a> </td>
<td><p>Defines a Digital Signature Algorithm (DSA) prime generation seed as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-signature.md">Signature</a> </td>
<td><p>Defines the root element of an <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>  compliant signature. <a href="element-signature.md"><strong>Signature</strong></a> is the unique root element for a provisioning file signature.</p></td>
</tr>
<tr class="odd">
<td><a href="element-signaturemethod.md">SignatureMethod</a> </td>
<td><p>Defines the algorithm used to generate the signature thumbprint in <a href="element-signaturevalue.md"><strong>SignatureValue</strong></a>  as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="even">
<td><a href="element-signaturevalue.md">SignatureValue</a> </td>
<td><p>Defines the signature thumbprint as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> . The algorithm used to generate <a href="element-signaturevalue.md"><strong>SignatureValue</strong></a> is defined in <a href="element-signaturemethod.md"><strong>SignatureMethod</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-signedinfo.md">SignedInfo</a> </td>
<td><p>Defines all signed content within the signature as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-transform.md">Transform</a> </td>
<td><p>Defines a transform applied to the digested data object prior to <a href="element-digestmethod.md"><strong>DigestMethod</strong></a>  as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
<tr class="odd">
<td><a href="element-transforms.md">Transforms</a> </td>
<td><p>Defines a an ordered list of transforms applied to the digested data object as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-x509certificate.md">X509Certificate</a> </td>
<td><p>Defines an X.509 compliant signature as defined in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="odd">
<td><a href="element-x509data.md">X509Data</a> </td>
<td><p>Defines one or more X.509 compliant signatures as defined in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a> .</p></td>
</tr>
<tr class="even">
<td><a href="element-y.md">Y</a> </td>
<td><p>Defines <a href="element-g.md"><strong>G</strong></a> **X mod <a href="element-p.md"><strong>P</strong></a> (where X is part of the private key and not made public) as specified in <a href="https://www.w3.org/TR/xmldsig-core/">XML DSIG</a>.</p></td>
</tr>
</tbody>
</table>

 

The full CarrierControlSignatureSchema schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>  
  
<schema xmlns="http://www.w3.org/2001/XMLSchema"  
        xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  
        targetNamespace="http://www.w3.org/2000/09/xmldsig#"  
        version="0.1" elementFormDefault="qualified">
  
<simpleType name="CryptoBinary">  
  <restriction base="base64Binary">  
  </restriction>  
</simpleType> 
  
<element name="Signature" type="ds:SignatureType"/>  
<complexType name="SignatureType">  
  <sequence>   
    <element ref="ds:SignedInfo"/>   
    <element ref="ds:SignatureValue"/>   
    <element ref="ds:KeyInfo" minOccurs="0"/>   
  </sequence>    
  <attribute name="Id" type="ID" use="optional"/>  
</complexType>  
  
  <element name="SignatureValue" type="ds:SignatureValueType"/>   
  <complexType name="SignatureValueType">  
    <simpleContent>  
      <extension base="base64Binary">  
        <attribute name="Id" type="ID" use="optional"/>  
      </extension>  
    </simpleContent>  
  </complexType>  
  
<element name="SignedInfo" type="ds:SignedInfoType"/>  
<complexType name="SignedInfoType">  
  <sequence>   
    <element ref="ds:CanonicalizationMethod"/>   
    <element ref="ds:SignatureMethod"/>   
    <element ref="ds:Reference"/>   
  </sequence>    
  <attribute name="Id" type="ID" use="optional"/>   
</complexType>  
  
  <element name="CanonicalizationMethod" type="ds:CanonicalizationMethodType"/>   
  <complexType name="CanonicalizationMethodType" mixed="true">  
    <attribute name="Algorithm" use="required">   
      <simpleType>  
        <restriction base="anyURI">  
          <enumeration value="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>  
          <enumeration value="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"/>  
          <enumeration value="http://www.w3.org/2001/10/xml-exc-c14n#"/>  
          <enumeration value="http://www.w3.org/2001/10/xml-exc-c14n#WithComments"/>  
        </restriction>  
      </simpleType>  
    </attribute>  
  </complexType>  
  
  <element name="SignatureMethod" type="ds:SignatureMethodType"/>  
  <complexType name="SignatureMethodType" mixed="true">  
    <sequence>  
      <element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>  
      <any namespace="##other" minOccurs="0" maxOccurs="unbounded"/>   
    </sequence>  
    <attribute name="Algorithm" type="anyURI" use="required"/>   
  </complexType>  
  
<element name="Reference" type="ds:ReferenceType"/>  
<complexType name="ReferenceType">  
  <sequence>   
    <element ref="ds:Transforms"/>   
    <element ref="ds:DigestMethod"/>   
    <element ref="ds:DigestValue"/>   
  </sequence>  
  <attribute name="Id" type="ID" use="optional"/>    
  <attribute name="URI">  
    <simpleType>  
      <restriction base="anyURI">  
        <maxLength value="0"/>  
      </restriction>        
    </simpleType>  
  </attribute>  
</complexType>  
  
  <element name="Transforms" type="ds:TransformsType"/>  
  <complexType name="TransformsType">  
    <sequence>  
      <element ref="ds:Transform" maxOccurs="1"/>    
    </sequence>  
  </complexType>  
  
  <element name="Transform" type="ds:TransformType"/>  
  <complexType name="TransformType" mixed="true">  
    <attribute name="Algorithm" use="required">   
      <simpleType>  
        <restriction base="anyURI">  
          <enumeration value="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>  
        </restriction>  
      </simpleType>  
    </attribute>  
  </complexType>  
  
<element name="DigestMethod" type="ds:DigestMethodType"/>  
<complexType name="DigestMethodType" mixed="true">   
  <sequence>  
    <any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>  
  </sequence>      
  <attribute name="Algorithm" type="anyURI" use="required"/>   
</complexType>  
  
<element name="DigestValue" type="ds:DigestValueType"/>  
<simpleType name="DigestValueType">  
  <restriction base="base64Binary"/>  
</simpleType>  
  
<element name="KeyInfo" type="ds:KeyInfoType"/>   
<complexType name="KeyInfoType" mixed="true">  
  <choice maxOccurs="unbounded">       
    <element ref="ds:KeyValue"/>   
    <element ref="ds:X509Data"/>   
    <any processContents="lax" namespace="##other"/> 
  </choice>  
  <attribute name="Id" type="ID" use="optional"/>   
</complexType>  
  
  
  <element name="KeyValue" type="ds:KeyValueType"/>   
  <complexType name="KeyValueType" mixed="true">  
   <choice>  
     <element ref="ds:DSAKeyValue"/>  
     <element ref="ds:RSAKeyValue"/>  
     <any namespace="##other" processContents="lax"/>  
   </choice>  
  </complexType>  

<element name="X509Data" type="ds:X509DataType"/>   
<complexType name="X509DataType">  
  <sequence maxOccurs="unbounded">  
    <choice>  
      <element name="X509Certificate" type="base64Binary"/>  
    </choice>  
  </sequence>  
</complexType>  

<simpleType name="HMACOutputLengthType">  
  <restriction base="integer"/>  
</simpleType>  
  
<element name="DSAKeyValue" type="ds:DSAKeyValueType"/>  
<complexType name="DSAKeyValueType">  
  <sequence>  
    <sequence minOccurs="0">  
      <element name="P" type="ds:CryptoBinary"/>  
      <element name="Q" type="ds:CryptoBinary"/>  
    </sequence>  
    <element name="G" type="ds:CryptoBinary" minOccurs="0"/>  
    <element name="Y" type="ds:CryptoBinary"/>  
    <element name="J" type="ds:CryptoBinary" minOccurs="0"/>  
    <sequence minOccurs="0">  
      <element name="Seed" type="ds:CryptoBinary"/>  
      <element name="PgenCounter" type="ds:CryptoBinary"/>  
    </sequence>  
  </sequence>  
</complexType>  
  
<element name="RSAKeyValue" type="ds:RSAKeyValueType"/>  
<complexType name="RSAKeyValueType">  
  <sequence>  
    <element name="Modulus" type="ds:CryptoBinary"/>   
    <element name="Exponent" type="ds:CryptoBinary"/>   
  </sequence>  
</complexType>   
</schema>  
```

 

 



