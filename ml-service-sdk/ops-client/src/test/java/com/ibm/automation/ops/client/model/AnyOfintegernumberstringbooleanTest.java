/*
 * IBM Confidential
 * OCO Source Materials
 * 5737-I23
 * Copyright IBM Corp. 2019, 2020
 * The source code for this program is not published or otherwise divested of its trade secrets, irrespective of what has been deposited with the U.S Copyright Office.
 */

package com.ibm.automation.ops.client.model;

import com.google.gson.Gson;
import com.ibm.automation.ops.client.JSON;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.LinkedHashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;


class AnyOfintegernumberstringbooleanTest {

    private static Gson mapper;

    @BeforeAll
    static void setUp() {
        JSON json = new JSON();
        mapper = json.getGson();
    }

    @Test
    @Tag("UnitTest")
    void shouldReadWriteToAnInteger() {
        // Arrange
        AnyOfintegernumberstringboolean value = new AnyOfintegernumberstringboolean(42);

        String stringValue = value.toString();

        // Act

        AnyOfintegernumberstringboolean readValue = mapper.fromJson(stringValue, AnyOfintegernumberstringboolean.class);

        // Assert
        assertEquals(42, value.getValue());
        assertEquals("42", stringValue);
        assertEquals(42, readValue.getValue());
    }


    @Test
    @Tag("UnitTest")
    void shouldReadWriteToADecimal() {
        // Arrange
        AnyOfintegernumberstringboolean value = new AnyOfintegernumberstringboolean(0.42);
        String stringValue = value.toString();

        // Act
        AnyOfintegernumberstringboolean readValue = mapper.fromJson(stringValue, AnyOfintegernumberstringboolean.class);

        // Assert
        assertEquals(new BigDecimal(0.42), value.getValue());
        assertTrue(stringValue.startsWith("0.4"));
        assertEquals(new BigDecimal(0.42), readValue.getValue());
    }

    @Test
    @Tag("UnitTest")
    void shouldReadWriteToABoolean() {
        // Arrange
        AnyOfintegernumberstringboolean value = new AnyOfintegernumberstringboolean(true);
        String stringValue = value.toString();

        // Act
        AnyOfintegernumberstringboolean readValue = mapper.fromJson(stringValue, AnyOfintegernumberstringboolean.class);

        // Assert
        assertEquals(true, value.getValue());
        assertEquals("true", stringValue);
        assertEquals(true, readValue.getValue());
    }

    @Test
    @Tag("UnitTest")
    void shouldReadWriteToAString() {
        // Arrange
        AnyOfintegernumberstringboolean value = new AnyOfintegernumberstringboolean("forty-two");
        String stringValue = value.toString();

        // Act
        AnyOfintegernumberstringboolean readValue = mapper.fromJson(stringValue, AnyOfintegernumberstringboolean.class);

        // Assert
        assertEquals("forty-two", value.getValue());
        assertEquals("forty-two", stringValue);
        assertEquals("forty-two", readValue.getValue());
    }

    @Test
    @Tag("UnitTest")
    void shouldProcessInputMap() {

        byte flagByte = 24;
        short sizeShort = 38;
        LinkedHashMap<String, Object> input = new LinkedHashMap<String, Object>() {{
            put("GENDER", "MALE");
            put("AGE", 45);
            put("MARRIED", true);
            put("WEIGHT", 80.689);
            put("BANK_ACCOUNT", 42949672960L);
            put("RANK", 1.2f);
            put("FLAG", flagByte);
            put("SIZE", sizeShort);
            put("WIFE_BANK_ACCOUNT", new BigDecimal(3.7778932e+22 + 0.15));
            put("WIFE_BANK_ACCOUNT2", new BigInteger("123456789123456789"));
            put("GRADE", 'C');
            put("LEVEL", null);
        }};

        AnyOfintegernumberstringboolean gender = AnyOfintegernumberstringboolean.build(input.get("GENDER"));
        AnyOfintegernumberstringboolean age = AnyOfintegernumberstringboolean.build(input.get("AGE"));
        AnyOfintegernumberstringboolean married = AnyOfintegernumberstringboolean.build(input.get("MARRIED"));
        AnyOfintegernumberstringboolean weight = AnyOfintegernumberstringboolean.build(input.get("WEIGHT"));
        AnyOfintegernumberstringboolean bankAccount = AnyOfintegernumberstringboolean.build(input.get("BANK_ACCOUNT"));
        AnyOfintegernumberstringboolean rank = AnyOfintegernumberstringboolean.build(input.get("RANK"));
        AnyOfintegernumberstringboolean flag = AnyOfintegernumberstringboolean.build(input.get("FLAG"));
        AnyOfintegernumberstringboolean size = AnyOfintegernumberstringboolean.build(input.get("SIZE"));
        AnyOfintegernumberstringboolean wifeBankAccount = AnyOfintegernumberstringboolean.build(input.get("WIFE_BANK_ACCOUNT"));
        AnyOfintegernumberstringboolean wifeBankAccount2 = AnyOfintegernumberstringboolean.build(input.get("WIFE_BANK_ACCOUNT2"));
        AnyOfintegernumberstringboolean grade = AnyOfintegernumberstringboolean.build(input.get("GRADE"));
        AnyOfintegernumberstringboolean level = AnyOfintegernumberstringboolean.build(input.get("LEVEL"));

        assertNotNull(gender);
        assertNotNull(age);
        assertNotNull(married);
        assertNotNull(weight);
        assertNotNull(bankAccount);
        assertNotNull(rank);
        assertNotNull(flag);
        assertNotNull(size);
        assertNotNull(wifeBankAccount);
        assertNotNull(wifeBankAccount2);
        assertNotNull(grade);
        assertNull(level);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.STRING, gender.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.INTEGER, age.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.BOOLEAN, married.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.NUMBER, weight.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.INTEGER, bankAccount.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.NUMBER, rank.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.INTEGER, flag.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.INTEGER, size.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.NUMBER, wifeBankAccount.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.NUMBER, wifeBankAccount2.type);
        assertEquals(AnyOfintegernumberstringboolean.AnyType.STRING, grade.type);
    }

    @Test
    @Tag("UnitTest")
    void shouldSerializeStringParameters() {
        // ARRANGE

        byte flagByte = 24;
        short sizeShort = 38;
        LinkedHashMap<String, Object> predictionInput = new LinkedHashMap<String, Object>() {{
            put("GENDER", "MALE");
            put("AGE", 45);
            put("MARRIED", true);
            put("WEIGHT", 80.689);
            put("BANK_ACCOUNT", 42949672960L);
            put("RANK", 1.2f);
            put("FLAG", flagByte);
            put("SIZE", sizeShort);
            put("WIFE_BANK_ACCOUNT", new BigDecimal(3.7778932e+22 + 0.15));
//            put("WIFE_BANK_ACCOUNT2", new BigInteger("123456789123456789"));
            put("GRADE", 'C');
            put("LEVEL", null);
        }};
        for (Map.Entry<String, Object> parameter : predictionInput.entrySet()) {
            testParameterReadWrite(new LinkedHashMap<String, Object>() {{
                put(parameter.getKey(), parameter.getValue());
            }});
        }

    }

    private void testParameterReadWrite(LinkedHashMap<String, Object> predictionInput) {
        Prediction prediction = new Prediction();

        for (Map.Entry<String, Object> entry : predictionInput.entrySet()) {
            Parameter p = new Parameter();
            p.setName(entry.getKey());
            p.setValue(AnyOfintegernumberstringboolean.build(entry.getValue()));
            prediction.addParametersItem(p);
        }

        // ACT
        String jsonString = mapper.toJson(prediction);

        Prediction deserializedPrediction = mapper.fromJson(jsonString, Prediction.class);

        // ASSERT
        assertFalse(jsonString.isEmpty());
        assertEquals(prediction.getParameters().get(0).getName(),
                deserializedPrediction.getParameters().get(0).getName());

        AnyOfintegernumberstringboolean o1 = prediction.getParameters().get(0).getValue();
        AnyOfintegernumberstringboolean o2 = deserializedPrediction.getParameters().get(0).getValue();
        if (o1 != null && o2 != null) {
            assertEquals(o1.getValue(), o2.getValue());
            assertEquals(o1.type, o2.type);
        }
        assertEquals(prediction.getParameters().get(0).getValue(),
                deserializedPrediction.getParameters().get(0).getValue());
    }
}