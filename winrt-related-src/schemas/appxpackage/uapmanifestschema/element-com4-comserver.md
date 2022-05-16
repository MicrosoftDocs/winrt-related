---
title: com4:ComServer
description: Declares a package extension point of type windows.comServer (com4:ComServer).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ComServer



## Description

Declares a package extension point of type windows.comServer. The comServer extension may include class registrations, including activation details for the servers that implement these classes, and ProgId and TreatAsClass registrations, which provide additional identifiers used to reference these classes at runtime.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-extension.md">&lt;com4:Extension&gt;</a></dt>
<dd>
<b>&lt;com4:ComServer&gt;</b>
</dd>
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
```syntax
<com4:ComServer>
<!-- Child elements -->
  Class{0,1}
  ExeServer{0,1}
  ServiceServer{0,1}
  SurrogateServer{0,1}
  TreatAsClass{0,1}
  ProgId{0,1}
  InProcessServer{0,1}
  InProcessHandler{0,1}
  ManagedInProcessServer{0,1}
  com5:InProcessServer{0,1}
  com5:InProcessHandler{0,1}
</com4:ComServer>
```

## Key
`{}`   specific range of occurrences




## Child Elements

| Element | Description |
| -----------| -------------|
| [Class](element-com4-class.md) | Defines a class registration in a COM server. |
| [ExeServer](element-com4-exeserver.md) | Registers an ExeServer with one or many class registrations. |
| [ServiceServer](element-com4-serviceserver.md) | Registers a ServiceServer with one or many class registrations. |
| [SurrogateServer](element-com4-surrogateserver.md) | Registers a SurrogateServer with one or many class registrations. |
| [TreatAsClass](element-com4-treatasclass.md) | A registration that corresponds to a CLSID registration with the TreatAs subkey. |
| [ProgId](element-com4-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. |
| [InProcessServer](element-com4-inprocessserver.md) | Registers an in-process server with one or many class registrations. |
| [InProcessHandler](element-com4-inprocesshandler.md) | Registers an in-process handler with one or many class registrations. |
| [ManagedInProcessServer](element-com4-managedinprocessserver.md) | Registers a managed in-process server with one or many class registrations. |
| [com5:InProcessServer](TBD) | TBD |
| [com5:InProcessHandler](TBD) | TBD |

## Remarks
In multi-application packages, it's important to place the COM server registration under the correct Applications/Application manifest element, because COM server processes will run with the identity of the ancestor Applications/Application element.

COM servers registered in the manifest always get Activate As Package (AAP) behavior, which means the COM server runs with the user session default token with package and application claims added. This is different from the default activation behavior of classically registered COM servers, in which the COM server runs with the client's token. For most applications, this difference will not be noticeable because clients typically run with the user session default token. Other activation behaviors, such as [RunAs]( /windows/win32/com/runas), are not supported.

It is possible to have multiple **comServer** extensions under the Applications/Application element, but in most cases this is neither necessary nor recommended. An example of an edge case where multiple **comServer** extensions are needed is if a package needs some of the registrations to have CompatMode="classic" while others have CompatMode="modern", the only way to do this is to split them between extensions.

### Changes in the com4 extension

The com4 extension syntax is a new, superset of the previous com extension syntax. This version of the syntax supports the same structure as older versions of the syntax, where class registrations are represented by ExeServer/Class, SurrogateServer/Class, ServiceServer/Class, InProcessServer/Class, InProcessHandler/Class, or ManagedInProcessServer/Class elements. 

The new syntax also supports alternative structures, where:

- ExeServer/ClassReference, SurrogateServer/ClassReference, ServiceServer/ClassReference, InProcessServer/ClassReference, InProcessHandler/ClassReference, or ManagedInProcessServer/ClassReference elements reference top-level Class elements
 
and/or

- SurrogateServer/InProcessServerClassReference elements reference InProcessServer/Class (alternatively, InProcessServer/ClassReference) or ManagedInProcessServer/Class (alternatively, ManagedInProcessServer/ClassReference) elements.

The main purpose of the new syntax structure is to enable combinations of in-process server, in-process handler, and out of process server registrations for the same CLSID, as is possible and supported with the classic registry layout. For more information on the COM registry layout, see [CLSID Key](/windows/win32/com/clsid-key-hklm).


## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
