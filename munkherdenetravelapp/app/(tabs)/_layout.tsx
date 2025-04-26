import {View, Text} from 'react-native';
import React from 'react';
import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';


export default function Layout(){
  return(
    <Tabs>
      <Tabs.Screen name= 'index' options={{tabBarIcon: ({color}) =>(
        <Ionicons name= 'compass' size={28} color={color}/>
      ),
      }}/>
      <Tabs.Screen name= 'category' options={{tabBarIcon: ({color}) =>(
        <MaterialIcons name= 'space-dashboard' size={28} color={color}/>
      ),
      }}/>
      <Tabs.Screen name= 'search' />
      <Tabs.Screen name= 'bookmarks' />
      <Tabs.Screen name= 'profile' />
    </Tabs>

  )
}
  