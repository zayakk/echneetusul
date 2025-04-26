import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  ActivityIndicator,
  FlatList,
  StyleSheet,
  Image,
  ScrollView,
  TouchableOpacity,
} from "react-native";
import { fetchData, ResponseInterface } from "../../../utils/needful";
import AntDesign from "@expo/vector-icons/AntDesign";
import { Pressable } from "react-native-gesture-handler";
import { Link, router } from "expo-router";

const HomeScreen = () => {
  const [response, setResponse] = useState<ResponseInterface | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchList();
  }, []);

  const fetchList = async () => {
    try {
      const data = await fetchData({
        url: "http://127.0.0.1:8000/user/",
        //url: "http://echnee.mandakh.org/user/",
        method: "POST",
        body: { action: "gethomepagedata" },
      });
      setResponse(data);
    } catch (err: any) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  const renderItem = ({ item }: { item: any }) => (
    <View>
      <View style={styles.card}>
        <View style={styles.cardLeft}>
          <Text style={styles.title}>{item.catname_mn}</Text>
        </View>
        <View style={styles.cardRight}>
          <Text style={styles.subtitle}>{item.bagts} багц </Text>
          <AntDesign name="right" size={14} color="black" />
        </View>
      </View>
      <ScrollView
        style={styles.subcatmain}
        showsHorizontalScrollIndicator={false}
        horizontal={true}
      >
        {item["subcat"].map((subcat, index) => (
          <TouchableOpacity
            style={styles.subcat}
            onPress={() =>
              router.push({
                pathname: "/category/[scid]",
                params: { scid: subcat.scid.toString() },
              })
            }
          >
            <View style={styles.subcatImage}>
              <View style={styles.subcatimagein}>
                <Image
                  style={styles.subcatimg}
                  source="https://cdn-icons-png.freepik.com/256/11441/11441082.png?semt=ais_hybrid"
                />
              </View>
            </View>
            <View style={styles.subcatcontainer}>
              <View style={styles.subcattitleview}>
                <Text style={styles.subcattitle}>{subcat.subname_en}</Text>
              </View>
              <View style={styles.subcatsubtitleview}>
                <Text style={styles.subcatsubtitle}>{subcat.subname_mn}</Text>
              </View>
            </View>
          </TouchableOpacity>
        ))}
      </ScrollView>
    </View>
  );

  const keyExtractor = (item: any) => item.cid.toString();

  if (loading)
    return <ActivityIndicator size="large" style={styles.centered} />;
  if (error) return <Text style={styles.errorText}>Error: {error}</Text>;
  if (response?.resultCode !== 200 || !response?.data?.length)
    return <Text style={styles.noDataText}>No data available.</Text>;

  return (
    <FlatList
      data={response.data}
      keyExtractor={keyExtractor}
      renderItem={renderItem}
      contentContainerStyle={styles.container}
    />
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    paddingBottom: 60,
    backgroundColor: "white",
  },
  card: {
    padding: 16,
    flex: 1,
    // backgroundColor: "#e3f2fd",
    marginBottom: 12,
    borderRadius: 8,
    elevation: 2,
    flexDirection: "row",
    alignItems: "center",
  },
  title: {
    fontWeight: "bold",
    fontSize: 16,
  },
  subtitle: {
    color: "#333",
    //marginTop: 4,
    // textAlign: "end",
    paddingLeft: 10,

    //alignContent: "center",
  },
  centered: {
    flex: 1,
    justifyContent: "center",
  },
  errorText: {
    color: "red",
    padding: 20,
    textAlign: "center",
  },
  noDataText: {
    padding: 20,
    fontSize: 16,
    textAlign: "center",
  },
  cardLeft: { flex: 6 },
  cardRight: {
    flex: 1,
    backgroundColor: "#ccc",
    borderRadius: 10,
    height: 30,
    alignItems: "center",
    flexDirection: "row",
  },
  subcatmain: { padding: 16 },
  subcat: {
    height: 140,
    width: 100,
    //backgroundColor: "#ccc",
    marginRight: 15,
    alignItems: "center",
  },
  subcatImage: {
    height: 100,
    width: 100,
    //backgroundColor: "#ccc123",
    //marginTop: 10,
    borderRadius: 5,
    borderColor: "pink",
    borderWidth: 3,
    padding: 5,
    alignItems: "center",
    justifyContent: "center",
  },
  subcatimg: {
    flex: 1,

    borderRadius: 10,
    margin: 5,
  },
  subcatimagein: {
    height: 80,
    width: 80,
    backgroundColor: "#eee",
    borderRadius: 5,
  },
  subcattitle: { color: "black", textAlign: "center", fontSize: 15 },
  subcatsubtitle: { color: "#999", textAlign: "center" },
  subcatcontainer: { alignItems: "center" },
  subcattitleview: { marginTop: 5 },
  subcatsubtitleview: { marginTop: 5 },
});

export default HomeScreen;
