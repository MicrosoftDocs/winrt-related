---
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, mobile broadband schema
---

# Plans schema


The Plans schema defines elements that are used to describe a subscriber's data plan on a Mobile Network Operator (MNO). All of the elements are in the namespace http://www.microsoft.com/networking/CarrierControl/Plans/v1. Not all elements are in every profile, as some elements are optional.

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
<td>[BillingCycle](element-billingcycle.md)</td>
<td><p>Defines the plan's starting date and time, its duration, and what happens at the end of the billing cycle. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="even">
<td>[DataLimitInMegabytes](element-datalimitinmegabytes.md)</td>
<td><p>Defines a value representing the data limit in MB for a capped plan. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="odd">
<td>[DataUsageInMobileOperatorNotificationEnabled](element-datausageinmobileoperatornotificationenabled.md)</td>
<td><p>Indicates whether the [<strong>NetworkOperatorNotificationTrigger</strong>](https://msdn.microsoft.com/library/windows/apps/br224831) should include data usage notifications. If <strong>true</strong>, Windows raises this trigger when the data usage threshold is met.</p></td>
</tr>
<tr class="even">
<td>[Description](element-description.md)</td>
<td><p>Defines plan information that specifies the subscriber's Mobile Network Operator (MNO) connection type.</p></td>
</tr>
<tr class="odd">
<td>[InboundBandwidthInKbps](element-inboundbandwidthinkbps.md)</td>
<td><p>Defines a value representing the effective link speed of the subscriber’s inbound connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="even">
<td>[MaxTransferSizeInMegabytes](element-maxtransfersizeinmegabytes.md)</td>
<td><p>Defines the size of an individual download in MB which a compliant application should permit over a metered connection without explicit user approval of the connection being used. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="odd">
<td>[OutboundBandwidthInKbps](element-outboundbandwidthinkbps.md)</td>
<td><p>Defines a value representing the effective link speed of the subscriber’s outbound connection specified in Kbps. Must be a value from 0 to 2<sup>32nd</sup>. Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="even">
<td>[Plan](element-plan.md)</td>
<td><p>Defines a set of plan information that specifies the data usage options and state of a subscriber's connection to a Mobile Network Operator (MNO). [<strong>Plan</strong>](element-plan.md) is the unique root element for plan information</p></td>
</tr>
<tr class="odd">
<td>[SecurityUpdatesExempt](element-plan.md)</td>
<td><p>If <strong>true</strong>, the MNO advises Windows Update (WU) that security updates are exempt from being counted as data usage against the subscriber’s plan and WU will download all security patches when on a metered network. Otherwise, WU will only download zero-day patches and not all security updates when <strong>false</strong>.</p></td>
</tr>
<tr class="even">
<td>[Usage](element-usage.md)</td>
<td><p>Defines the state of a subscriber's data usage on a connection to a Mobile Network Operator (MNO). Windows Store apps can retrieve this information using the [<strong>DataPlanStatus</strong>](https://msdn.microsoft.com/library/windows/apps/br207256) class.</p></td>
</tr>
<tr class="odd">
<td>[UserSMSEnabled](element-usersmsenabled.md)</td>
<td><p>Indicates whether the subscriber's service includes user-to-user SMS which must be delivered in near real-time. If <strong>true</strong>, Windows will employ less aggressive power management on the Mobile Broadband interface to allow SMS messages to arrive more quickly. If <strong>false</strong>, the mobile broadband radio may be turned off during periods of inactivity. SMS messages will arrive when the PC is next active.</p></td>
</tr>
</tbody>
</table>

 

The full Plans schema is below:

``` syntax
<?xml version="1.0" encoding="utf-8"?>  
<xs:schema targetNamespace="http://www.microsoft.com/networking/CarrierControl/Plans/v1"  
    elementFormDefault="qualified"  
    xmlns="http://www.microsoft.com/networking/CarrierControl/Plans/v1"  
    xmlns:xs="http://www.w3.org/2001/XMLSchema"  
    xmlns:base="http://www.microsoft.com/networking/CarrierControl/Base/v1">  
  
  <xs:import namespace="http://www.microsoft.com/networking/CarrierControl/Base/v1"/>  
   
  <xs:complexType name="BillingCycleType">  
    <xs:attribute name="StartDate" type="xs:dateTime" use="required"/>  
    <xs:attribute name="Duration" use="required">  
      <xs:simpleType>  
        <xs:restriction base="xs:duration">  
          <xs:minExclusive value="PT0S"/>  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
    <xs:attribute name="Resets" type="xs:boolean" default="true"/>  
  </xs:complexType>  
  
  <xs:simpleType name="PlanType">  
    <xs:annotation>  
      <xs:documentation>  
        PlanType expresses the incremental cost of a plan:  
          - Unrestricted:  There is no incremental cost for consumption on this plan  
          - Fixed:  Consumption goes against a quota which the user has purchased / agreed to purchase  
          - Variable:  The user will be billed for incremental usage on this plan  
      </xs:documentation>  
    </xs:annotation>  
    <xs:restriction base="xs:string">  
      <xs:enumeration value="Unrestricted"/>  
      <xs:enumeration value="Fixed"/>  
      <xs:enumeration value="Variable"/>  
    </xs:restriction>  
  </xs:simpleType>  
  
  <xs:element name="Plan">  
    <xs:complexType>  
      <xs:choice>  
        <xs:sequence>  
          <xs:element ref="Description"/>  
          <xs:element ref="Usage" minOccurs="0"/>  
        </xs:sequence>  
        <xs:sequence>  
          <xs:element ref="Usage"/>  
        </xs:sequence>  
      </xs:choice>  
      <xs:attribute type="xs:string" name="Name" use="required"/>  
    </xs:complexType>  
  </xs:element>   
  
  <xs:element name="Description" type="DescriptionBaseType"/>  
  <xs:complexType name="DescriptionBaseType">  
    <xs:sequence>  
      <xs:element name="BillingCycle" type="BillingCycleType" minOccurs="0"/>  
      <xs:element name="DataLimitInMegabytes" type="xs:positiveInteger" minOccurs="0"/>  
      <xs:element name="InboundBandwidthInKbps" type="xs:nonNegativeInteger" minOccurs="0"/>  
      <xs:element name="OutboundBandwidthInKbps" type="xs:nonNegativeInteger" minOccurs="0"/>  
      <xs:element name="MaxTransferSizeInMegabytes" type="xs:positiveInteger" minOccurs="0"/>  
      <xs:element name="SecurityUpdatesExempt" type="xs:boolean" default="false" minOccurs="0"/>  
      <xs:element name="DataUsageInMobileOperatorNotificationEnabled" type="xs:boolean" default="false" minOccurs="0"/>  
      <xs:element name="UserSMSEnabled" type="xs:boolean" default="true" minOccurs="0"/>  
    </xs:sequence>  
    <xs:attribute type="PlanType" name="PlanType" use="required"/>  
  </xs:complexType>  
  
  <xs:element name="Usage" type="PlanUsageType"/>  
  <xs:complexType name="PlanUsageType">  
    <xs:attribute name="OverLimit" type="xs:boolean"/>  
    <xs:attribute name="Congested" type="xs:boolean"/>  
    <xs:attribute name="CurrentUsage" type="xs:nonNegativeInteger" use="required"/>  
    <xs:attribute name="UsageTimestamp" type="xs:dateTime" use="required"/>  
  </xs:complexType>  
</xs:schema>
```

 

 



