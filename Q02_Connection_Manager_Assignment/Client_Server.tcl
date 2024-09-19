namespace eval ConectionManager {
    variable ServerUp 0
    variable client1Up 0
    variable client2Up 0
    variable clientlist ""
    variable Msg ""
    variable prefix1 "abcd"
    variable prefix2 "abcdefgh"
    variable suffix1 "ABCDE"
    variable suffix2 "ABCDEFGHIJ"

    proc StartServer {} {
        set ConectionManager::ServerUp 1
    }

    proc StartClient1 {} {
        set ConectionManager::client1Up 1
    }

    proc StartClient2 {} {
        set ConectionManager::client2Up 1
    }

    proc ConnectClient1 {} {
        lappend ConectionManager::clientlist 1
    }

    proc ConnectClient2 {} {
        lappend ConectionManager::clientlist 2
    }

    proc CloseServer {} {
        set ConectionManager::ServerUp 0
    }

    proc CloseClient1 {} {
        set ConectionManager::client1Up 0
    }

    proc CloseClient2 {} {
        set ConectionManager::client2Up 0
    }

    proc ConstructMsg {prefixType msgBody suffixType} {
        set msg ""

        # Add prefix
        switch $prefixType {
            1 {
                set msg $ConectionManager::prefix1
                set maxMsgLength 34
            }
            2 {
                set msg $ConectionManager::prefix2
                set maxMsgLength 38
            }
            default {
                puts "Unknown prefix!"
            }
        }

        # Add message body
        set msg "$msg$msgBody"

        # Trim message if necessary
        if {[string length $msg] > $maxMsgLength} {
            set msg [string range $msg 0 $maxMsgLength]
        }

        set msglength [string length $msg]

        # Add suffix
        switch $suffixType {
            0 {
                set ConectionManager::Msg $msg
            }
            1 {
                set ConectionManager::Msg [string replace $msg [expr $msglength - 5] $msglength $ConectionManager::suffix1]
            }
            2 {
                set ConectionManager::Msg [string replace $msg [expr $msglength - 10] $msglength $ConectionManager::suffix2]
            }
            default {
                puts "Unknown suffix!"
            }
        }
    }

    proc BroadCast {} {
        foreach client $ConectionManager::clientlist {
            # Some code to send message
            puts "message $ConectionManager::Msg was sent to client $client"
        }
    }
}

#________________________________________________________________________________
# Example for testing
ConectionManager::StartServer
ConectionManager::StartClient1
ConectionManager::ConnectClient1
ConectionManager::StartClient2
ConectionManager::ConnectClient2
ConectionManager::CloseServer
ConectionManager::ConstructMsg 1 "123456789" 0
ConectionManager::BroadCast
ConectionManager::ConstructMsg 2 "123456789012345678901234567890" 1