---
author: laurenhughes
ms.assetid: 62d02a56-5e34-4b0a-93d5-f4fbec23e0bb
title: com:ComServer
description: Declares a package extension point of type windows.comServer.
ms.author: lahugh
ms.date: 03/29/2017
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, schema, manifest, com
---

# com:ComServer

## -description
Declares a package extension point of type **windows.comServer**. The **comServer** extension may include four types of registrations: **ExeServer**, **SurrogateServer**, **ProgId**, or **TreatAsClass**.

## -element-hierarchy
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
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd><b>&lt;com:ComServer&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## -syntax
```syntax
<ComServer>
  <!-- Child elements -->
  ( com:ExeServer{0,1000},
  com:SurrogateServer{0,1000},
  com:ProgId{0,10000},
  com:TreatAsClass{0,10000}
  )
</ComServer>
```

## -key
`{}`   specific range of occurrences

## -child-elements

| Child Element | Description |
|---------------|-------------|
| [ExeServer](element-com-exeserver.md) | Registers an ExeServer with one or many class registrations. |
| [SurrogateServer](element-com-surrogateserver.md) | Registers an SurrogateServer with one or many class registrations. |
| [ProgId](element-com-progid.md) | A programmatic identifier (ProgID) that can be associated with a CLSID. |
| [TreatAsClass](element-com-treatasclass.md) | A registration that corresponds to a CLSID registration with the TreatAs subkey. | 


## -remarks
In multi-application packages, it's important to place the COM server registration under the correct Applications/Application manifest element, because COM server processes will run with the identity of the ancestor Applications/Application element.

For multi-application packages:
- If an [AppID](https://msdn.microsoft.com/library/windows/desktop/ms682359.aspx) key contains an [AppId](https://msdn.microsoft.com/library/windows/desktop/ms688754.aspx) value, place all COM server registrations associated with the AppID key under the Applications/Application manifest element with the **Id** attribute that matches the **ApplicationId** value.
- If the [AppId](https://msdn.microsoft.com/library/windows/desktop/ms688754.aspx) is not specified in the package's private registry hive, you must group COM servers manually by application. 

COM servers have two main behaviors:
- Activate As Package (AAP) behavior is the default behavior of packaged COM registrations in the manifest. The COM server runs with the default session token with package and application claims added.
- Activate As Activator (AAA) is the default behavior when COM servers do not specify the [AppId](https://msdn.microsoft.com/library/windows/desktop/ms688754.aspx). AAA means that COM launches one instance of the COM server process for each distinct client token. For example, if Word and Excel both activate a PowerPoint COM server registered in the package's private registry hive as AAA, they would get separate instances of PowerPoint (one with Word's identity and one with Excel's identity).

Based on the behaviors described above, adding an [AppId](https://msdn.microsoft.com/library/windows/desktop/ms688754.aspx) to the package for the first time may change the instancing behavior of COM servers.

> [!NOTE]
> Any registrations in **comServer** that depend on another registration (e.g. a **ProgId** references a **Class**) must be in the same **comServer** extension. 

It is possible to have multiple **comServer** extensions under the Applications/Application element, but that is neither necessary nor recommended.

## -examples

## -requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>

