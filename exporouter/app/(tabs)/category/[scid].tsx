import React from "react";
import {
  View,
  Text,
  ActivityIndicator,
  StyleSheet,
  Button,
} from "react-native";
import { useLocalSearchParams, router } from "expo-router";

const Subcatpage = () => {
  const { scid } = useLocalSearchParams();

  if (!scid) {
    return (
      <View style={styles.container}>
        <Text style={styles.error}>SCID not found</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Category ID: {scid}</Text>

      <Button title="Back" onPress={() => router.back()} />
    </View>
  );
};

export default Subcatpage;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 24,
    justifyContent: "center",
    alignItems: "center",
  },
  title: {
    fontSize: 24,
    marginBottom: 16,
    fontWeight: "bold",
  },
  error: {
    fontSize: 18,
    color: "red",
  },
});
