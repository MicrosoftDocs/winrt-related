---

title: desktop6:Service
description: Specifies a service that is installed and registered along with the app. These services can be configured to run under either the Local Service, Network Service or Local System account.

ms.date: 04/19/2019
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop6:Service

## Description
Specifies a service that is installed and registered along with the app. These services can be configured to run under either the Local Service, Network Service or Local System account.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop6-extension.md">&lt;desktop6:Extension&gt;</a></dt>
<dd><b>&lt;desktop6:Service&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```xml
<desktop6:Service   Name          =  A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
                    StartupType   =  The following values are supported: auto, manual, disabled
                    StartAccount  =  The following values are supported: localSystem, localServices, networkService.
                    Arguments?     =  A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >
    desktop6:Dependencies?
    desktop6:TriggerEvents?
</desktop6:Service>
```

### Key
`?` optional (zero or one)

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | The name of the service. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |
| StartupType  | The startup type for the service.  | The following values are supported: **auto**, **manual**, **disabled**  | Yes |
| StartAccount | The type of account in which to run the service. | The following values are supported: **localSystem**, **localServices**, **networkService** | Yes |
| Arguments | Optional arguments to pass to the service. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop6:Dependencies](element-desktop6-dependencies.md) | Specifies one or more dependent services. |  
| [desktop6:TriggerEvents](element-desktop6-triggerevents.md) | Specifies one or more trigger event for the service. |  

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extension](element-desktop6-extension.md) | Defines an extensibility point for the application. |  


## Remarks

This element requires the **packagedServices** or **localSystemServices** [restricted capability](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities).


## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/6` |