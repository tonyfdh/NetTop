from pysnmp.hlapi import *

def snmp_walk(host, oid):
    """
    Perform an SNMP walk on the given host using the specified OID.
    """
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)),
               lexicographicMode=False)
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))

if __name__ == "__main__":
    host = '192.168.1.1'  # Replace this with the IP address of your SNMP-enabled device
    oid = '1.3.6.1.2.1'   # Replace this with the OID you want to walk (e.g., 1.3.6.1.2.1 for system info)

    snmp_walk(host, oid)