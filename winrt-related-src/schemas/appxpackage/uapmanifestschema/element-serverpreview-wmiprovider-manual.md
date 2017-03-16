---
Description: Identifies a Windows Management Instrumentation (WMI) provider to install, update, or uninstall out-of-band on Nano Server.
MS-HAID: UapManifestSchema.element\_serverpreview\_wmiprovider\_manual
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:WmiProvider
ms.assetid: 9268ed23-e619-4316-8a13-a13462e27479
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# serverpreview:WmiProvider


Identifies a Windows Management Instrumentation (WMI) provider to install, update, or uninstall out-of-band on Nano Server.

## Element hierarchy

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
<dt><a href="element-serverpreview-extension-manual.md">&lt;serverpreview:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-wmiproviders-manual.md">&lt;serverpreview:WmiProviders&gt;</a></dt>
<dd><b>&lt;serverpreview:WmiProvider&gt;</b></dd>
</dl>									
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


```
<serverpreview:WmiProvider Name =                         A string between 1 and 
                                                          1,024 characters in 
                                                          length with a non-
                                                          whitespace character 
                                                          at its beginning and 
                                                          end.
                           Namespace                    = A string between 1 and 
                                                          1,024 characters in 
                                                          length with a non-
                                                          whitespace character 
                                                          at its beginning and 
                                                          end.
                           HostingSpecfication          = "selfHost" |
                                                          "decoupled:Com" |
                                                          "localSystemHost" |
                                                          "localSystemHostOrSelfHost" |
                                                          "networkServiceHost" |
                                                          "localServiceHost" |
                                                          "networkServiceHostOrSelfHost"
                           HostingGroup?                = A string between 1 and 
                                                          256 characters in 
                                                          length with a non-
                                                          whitespace character 
                                                          at its beginning and 
                                                          end.
                           DecoupledProviderExecutable? = A string between 1 and 
                                                          256 characters in 
                                                          length that must end 
                                                          with ".exe" and cannot 
                                                          contain these 
                                                          characters: <, >, :, ",
                                                          |, ?, or *. >
  <!-- Child elements -->
  serverpreview:Mof{1,100}
</serverpreview:WmiProvider>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td>The name of the WMI provider to install, update, or uninstall out-of-band on Nano Server.</td>
<td>A string between 1 and 1,024 characters in length with a non-whitespace character at its beginning and end.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Namespace</strong></td>
<td>The namespace for the WMI provider</td>
<td>A string between 1 and 1,024 characters in length with a non-whitespace character at its beginning and end.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>HostingSpecification</strong></td>
<td>The first component of the <strong>HostingModel</strong> property of the [<strong>__Win32Provider</strong>](https://msdn.microsoft.com/library/aa394688) class, specifies how WMI loads the provider and the security account it runs under.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>selfHost</li>
<li>decoupled:Com</li>
<li>localSystemHost</li>
<li>localSystemHostOrSelfHost</li>
<li>networkServiceHost</li>
<li>localServiceHost</li>
<li>networkServiceHostOrSelfHost</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>HostingGroup</strong></td>
<td><p>The hosting group for the provider which is the second component of the <strong>HostingModel</strong> property of the [<strong>__Win32Provider</strong>](https://msdn.microsoft.com/library/aa394688) class, and specifies how WMI loads the provider and the security account it runs under.</p>
<p>A hosting group defines grouping of providers in a separate Wmiprvse.exe process. The manifest schema does not support the case where WMI providers from different packages that share the same shared hosting model also share the same Wmiprvse.exe process. For example, specifying a <strong>HostingSpecification</strong> of &quot;localSystemHost&quot; without any <strong>HostingGroup</strong> is not supported. So, the value of the <strong>HostingGroup</strong> attribute must be non-empty if the value of the <strong>HostingSpecification</strong> attribute is not &quot;SelfHost&quot; or &quot;Decoupled:Com&quot;.</p>
<p>The <strong>HostingGroup</strong> must be unique within the package and across all packages in the system.</p></td>
<td>A string between 1 and 256 characters in length with a non-whitespace character at its beginning and end.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>DecoupledProviderExecutable</strong></td>
<td>The executable file for a decoupled provider that is hosted in a separate process that is a client to WMI.</td>
<td>A string between 1 and 256 characters in length that must end with &quot;.exe&quot; and cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

**Child Elements**

| Child Element                                                 | Description                                                                                      |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**serverpreview:Mof**](element-serverpreview-mof-manual.md) | Specifies the Managed Object Format (MOF) files to use to install or uninstall the WMI provider. |

 

**Parent Elements**

| Parent Element                                                                  | Description                                                           |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**serverpreview:WmiProviders**](element-serverpreview-wmiproviders-manual.md) | Declares an app extensibility point of type **windows.wmiProviders**. |

 

## Remarks


The WMI provider extension is only available only on the Windows Server platform. This extension is ignored on other platforms.

The WMI provider extension supports both version 1 and version 2 WMI providers.

The combination the namespace and name for the WMI provider must be unique in the package and across the whole system. Deployment fails if another WMI provider with the same name under the same namespace exists in the same package.

## Examples


```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
        <Application>
            <Extensions>
                <serverpreview:Extension Category="windows.wmiProviders">  
                    <serverpreview:WmiProviders>  
                        <serverpreview:WmiProvider 
                                Name="ProviderName"
                                Namespace="root\standardcimv2"
                                HostingSpecification="networkServiceHost"
                                HostingGroup="ProviderGroup">  
                            <serverpreview:Mof 
                                    InstallMof="Install.mof"
                                    UninstallMof="Uninstall.mof"/>  
                        </serverpreview:WmiProvider>  
                        <serverpreview:WmiProvider  
                                Name="ProviderName2"  
                                Namespace="root\standardcimv2"
                                HostingSpecification="decoupled:Com"
                                DecoupledProviderExecutable="serviceExec.exe">  
                            <serverpreview:Mof  
                                    InstallMof="Install2.mof"  
                                    UninstallMof="Uninstall2.mof"/>  
                        </serverpreview:WmiProvider>  
                    </serverpreview:WmiProviders>  
                </serverpreview:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                                    |
|---------------|--------------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/serverpreview/windows10 |

 

 

 



