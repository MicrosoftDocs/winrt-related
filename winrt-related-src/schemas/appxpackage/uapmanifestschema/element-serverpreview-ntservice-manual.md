---
Description: Identifies an NT Service to install, update, or uninstall on Nano Server.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:NTService
ms.assetid: 4ce23453-fffb-47a0-aa32-8d2b900de356


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:NTService


Identifies an NT Service to install, update, or uninstall on Nano Server.

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
<dt><a href="element-serverpreview-ntservices-manual.md">&lt;serverpreview:NTServices&gt;</a></dt>
<dd><b>&lt;serverpreview:NTService&gt;</b></dd>
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
<serverpreview:NTService Name                   = A string between 1 and 256 
                                                  characters in length with a 
                                                  non-whitespace character at  
                                                  its beginning and end.
                         Executable             = string between 1 and 256 
                                                  characters in length that must
                                                  end with ".exe" and cannot 
                                                  contain these characters: <, 
                                                  >, :, ", |, ?, or *. 
                         StartupType            = "auto" | "manual"
                         StartAccount           = "localSystem" | 
                                                  "localService" |
                                                  "networkService"
                         DisplayName?           = A string between 1 and 256 
                                                  characters in length with a 
                                                  non-whitespace character at  
                                                  its beginning and end.
                         StartErrorAction?      = "ignoreError" | "logError"
                         StartParameters?       = A string between 1 and 32,767 
                                                  characters in length with a 
                                                  non-whitespace character at  
                                                  its beginning and end.
                         Description?           = A string between 1 and 32,767 
                                                  characters in length with a 
                                                  non-whitespace character at  
                                                  its beginning and end.
                         FailureRecoveryAction? = "none" | "restartService" >
  <!-- Child elements -->
  serverpreview:ServiceDependencies?
  serverpreview:ServiceParameters?
</serverpreview:NTService>
```

**Key**

          ? optional (zero or one)

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
<td>The name of the service to install, update, or uninstall. This name must be unique to the package.</td>
<td>A string between 1 and 256 characters in length with a non-whitespace character at its beginning and end.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Executable</strong></td>
<td>The name of the executable file for the service. The executable file must be included in the package. If this file is not include, the service fails to start.</td>
<td>A string between 1 and 256 characters in length that must end with &quot;.exe&quot; and cannot contain these characters: &lt;, &gt;, :, &quot;, |, ?, or *.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>StartupType</strong></td>
<td>The time at which to start the service, either automatically at system start or when a process manually requests the service start.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li><p>auto</p>
<p>Corresponds to the <strong>SERVICE_AUTO_START</strong> value for the <em>dwStartType</em> parameter of the [<strong>CreateService</strong>](https://msdn.microsoft.com/library/windows/desktop/ms682450) function.</p></li>
<li><p>manual</p>
<p>Corresponds to the <strong>SERVICE_DEMAND_START</strong> value for the <em>dwStartType</em> parameter of the [<strong>CreateService</strong>](https://msdn.microsoft.com/library/windows/desktop/ms682450) function.</p></li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>StartAccount</strong></td>
<td>The name of the account under which the service should start running.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li>localSystem</li>
<li>localService</li>
<li>networkService</li>
</ul></td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>DisplayName</strong></td>
<td>The display name for the service. This display name must be unique to the package.</td>
<td>A string between 1 and 256 characters in length with a non-whitespace character at its beginning and end.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>StartErrorAction</strong></td>
<td>The action to take when an error occurs while the service starts.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li><p>ignoreError</p>
<p>Corresponds to the <strong>SERVICE_ERROR_IGNORE</strong> value for the <em>dwErrorControl</em> parameter of the [<strong>CreateService</strong>](https://msdn.microsoft.com/library/windows/desktop/ms682450) function.</p></li>
<li><p>logError</p>
<p>Corresponds to the <strong>SERVICE_ERROR_NORMAL</strong> value for the <em>dwErrorControl</em> parameter of the [<strong>CreateService</strong>](https://msdn.microsoft.com/library/windows/desktop/ms682450) function.</p></li>
</ul></td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>StartParameters</strong></td>
<td>The command-line parameters to pass to the executable for the service when starting the service.</td>
<td>A string between 1 and 32,767 characters in length with a non-whitespace character at its beginning and end.</td>
<td>No</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td>The description for the service.</td>
<td>A string between 1 and 32,767 characters in length with a non-whitespace character at its beginning and end.</td>
<td>No</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>FailureRecoveryAction</strong></td>
<td>The action the server should take to try to recover when the service fails.</td>
<td><p>This attribute can have one of the following values:</p>
<ul>
<li><p>none</p>
<p>Corresponds to the <strong>SERVICE_ACTION_NONE</strong> value for the <strong>Type</strong> member of the [<strong>SC_ACTION</strong>](https://msdn.microsoft.com/library/windows/desktop/ms685126) structure.</p></li>
<li><p>restartService</p>
<p>Corresponds to the <strong>SERVICE_ACTION_RESTART</strong> value for the <strong>Type</strong> member of the [<strong>SC_ACTION</strong>](https://msdn.microsoft.com/library/windows/desktop/ms685126) structure.</p></li>
</ul></td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

 

**Child Elements**

| Child Element                                                                                 | Description                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:ServiceDependencies**](element-serverpreview-servicedependencies-manual.md) | Specifies the set of additional services on which the service that corresponds to the parent serverpreview:NTService element depends.                                                                                               |
| [**serverpreview:ServiceParameters**](element-serverpreview-serviceparameters-manual.md)     | Specifies a set of parameters to configure for the service. These parameters correspond to registry values that are created under the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\*ServiceName*\\Parameters** key. |

 

**Parent Elements**

| Parent Element                                                              | Description                                                         |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------|
| [**serverpreview:NTServices**](element-serverpreview-ntservices-manual.md) | Declares an app extensibility point of type **windows.ntServices**. |

 

## Remarks


The NT Service extension is only available only on the Windows Server platform. This extension is ignored on other platforms.

Only NT services that run in their own processes are supported. Services that share a service host or run as drivers are not supported. Actions like boot start and reboot on failure are not supported. Services must be standalone entities that can be restarted and deleted without affecting other applications.

## Examples


```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
       <Application Id="TestService">
            <uap:VisualElements AppListEntry="none" 
                                DisplayName="TestService" 
                                Square150x150Logo="logo.png" 
                                Square44x44Logo="logo.png" 
                                Description="TestService" 
                                BackgroundColor="#777777"/>
            <Extensions>
                <serverpreview:Extension Category="windows.ntServices">  
                    <serverpreview:NTServices>     
                        <serverpreview:NTService          
                                Name="serviceName"                     
                                Executable="serviceExec.exe"
                                StartupType="auto"  
                                DisplayName="service Display Name"  
                                StartErrorAction="ignoreError" 
                                StartAccount="localService"    
                                Description="service1 description"   
                                StartParameters="arg1 arg2"
                                FailureRecoveryAction="restartService"> 
                        </serverpreview:NTService> 
                    </serverpreview:NTServices>  
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

 

 

 



