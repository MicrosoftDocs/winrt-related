---
title: desktop6:Service
description: Specifies a service that is installed and registered along with the app. These services can be configured to run under either the Local Service, Network Service or Local System account.
ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:Service

Specifies a service that is installed and registered along with the app. These services can be configured to run under either the Local Service, Network Service or Local System account.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop6:Extension\>](element-desktop6-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop6:Service\>**

## Syntax

```xml
<desktop6:Service
    Name = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
    StartupType = 'A string that can be one of the following values: "auto", "manual", "disabled", or "delayedStart".'
    StartAccount = 'A string that can be one of the following values: "localSystem", "localService", or "networkService".'
    Arguments = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

    desktop6:Dependencies?
    desktop6:TriggerEvents?

</desktop6:Service>
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | The name of the service. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **StartupType**  | The startup type for the service.  | A string that can be one of the following values: *auto*, *manual*, *disabled*, or *delayedStart*. | Yes |  |
| **StartAccount** | The type of account in which to run the service. | A string that can be one of the following values: *localSystem*, *localServices*, or *networkService*. | Yes |  |
| **Arguments** | Optional arguments to pass to the service. | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop6:Dependencies](element-desktop6-dependencies.md) | Specifies one or more dependent services. |  
| [desktop6:TriggerEvents](element-desktop6-triggerevents.md) | Specifies one or more trigger event for the service. |  

### Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-desktop6-extension.md) | Defines an extensibility point for the application. |  

## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |
| **Minimum OS Version** | Windows 10 version 1903 (Build 18362) |
