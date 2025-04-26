import { Stack } from "expo-router";

export default function HomeStack() {
  return (
    <Stack initialRouteName="index">
      <Stack.Screen
        name="index"
        options={{ headerTitle: "Home 1", headerShown: false }}
      />
      <Stack.Screen
        name="[scid]"
        options={{ headerTitle: "Home 2", headerShown: false }}
      />
    </Stack>
  );
}
