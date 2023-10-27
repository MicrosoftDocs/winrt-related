---
title: com4:InProcessServerClassReference
description: Specifies the class or class reference with which the registered in-process server is associated and sets registration details. (com4:InProcessServerClassReference)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessServerClassReference

Specifies the class or class reference with which the registered in-process server is associated and sets registration details.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:SurrogateServer\>](element-com4-surrogateserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:InProcessServerClassReference\>**

## Syntax

```xml
<com4:InProcessServerClassReference
  EnableOleDefaultHandler = 'A boolean value.'
  Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **EnableOleDefaultHandler** | This should be set to true if the default value of the [InprocHandler32](/windows/win32/com/inprochandler32) key is `Ole32.dll`. Otherwise it should be omitted. | A boolean value. | Yes | False |
| **Id** | The Id of the [Class](element-com4-class.md) being referenced. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com4:SurrogateServer](element-com4-surrogateserver.md) | Registers a SurrogateServer with one or many class registrations. |

## Remarks

The CLSID Key](/windows/win32/com/clsid-key-hklm) in the COM registry layout enables a CLSID to be registered for inproc activation ([CLSCTX_INPROC_SERVER](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx)) and for outofproc activation in a surrogate server ([CLSCTX_LOCAL_SERVER](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx)) by specifying:

- Inproc activation details in an [InprocServer32](/windows/win32/com/inprocserver32) subkey.
- A reference to an AppID key via the AppID value of the CLSID key, where the AppID key specifies a surrogate via the [DllSurrogate](/windows/win32/com/dllsurrogate) value. Note that for outofproc activation in a surrogate server, the inproc server registration details, e.g. dll path and [ThreadingModel](/windows/win32/com/choosing-the-threading-model), are also used in outofproc activation. The **ClassReference** child of the [InProcessServer](element-com4-inprocessserver.md) element enables a package that registers a CLSID for both inproc and outofproc activation to specify the inproc server details once, as an [InProcessServer/Class](element-com4-inprocessserver-class.md) or **InProcessServer/ClassReference** element, and reference this element from the SurrogateServer that supports outofproc activation of the CLSID. This structure for the inproc/outofproc registrations more closely reflects the COM registry layout than independently specifying the dll path and ThreadingModel in both InProcessServer/ClassReference and SurrogateServer/ClassReference elements.

When packaging an application with a CLSID registered for outofproc activation in a surrogate server, it is generally recommended that only the surrogate server is registered in the manifest. For example, surrogate registrations are often used to support COM-based extension points that historically enabled inproc server implementations but which now recommend an outofproc server registration as a best practice for isolation. For packaged applications, there are additional functional limitations for inproc servers (see [In-ProcessServers](/windows/win32/com/in-process-servers) for details), whereas any package with the [runFullTrust restricted capability](/windows/uwp/packaging/app-capability-declarations) can successfully register a surrogate server, and for most extension points registering a surrogate server is sufficient to enable the functionality of the extension. However, if a packaged application needs to support inproc activation of its CLSIDs for compatibility with other applications that request inproc activation (CLSCTX_INPROC_SERVER), and satisfies the requirements for registering an inproc server, it can register the CLSID for inproc activation and outofproc activation in a surrogate. In this case, it is recommended to provide the inproc server details in an **InProcessServer/Class** or **InProcessServer/ClassReference** element, and reference them from a [SurrogateServer](element-com4-serviceserver.md)/[InProcessServerClassReference](element-com4-inprocessserverclassreference.md) element.

## Examples

The following example illustrates using **InProcessServerClassreference** to reference a class in a surrogate server registration.

```xml
<com4:Class Id="d57899b9-1334-4600-904a-719df0512988" DisplayName="CLSID_Baz"/> 
<com4:InProcessServer Path="MyServer.dll"> 
  <com4:ClassReference Id="d57899b9-1334-4600-904a-719df0512988" ThreadingModel="Apartment"/> 
</com4:InProcessServer> 
<com:SurrogateServer DisplayName="My surrogate server"> 
  <com4:InProcessServerClassReference Id="d57899b9-1334-4600-904a-719df0512988"/> 
</com:SurrogateServer> 
```

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| Minimum OS Version | Windows 10 (Build 20348) |
